#!/bin/sh

if [ ! -n "$PARENT" ]; then
	echo "~this script shouldn't be called separately!"
	exit 1
fi
echo "called by $PARENT"

########################################################################
HEADER_SIZE=0x100
RESERV0_SIZE=256
RESERV1_SIZE=3840

INPUT_DIR=../input
OUTPUT_DIR=../output
SOURCE_FILE=$INPUT_DIR/$SOURCE_NAME

#temporary variables
TEMP_I=$INPUT_DIR/tmp
TEMP_O=$OUTPUT_DIR/tmp

if [ ! -d $TEMP_I ]; then
	echo "~create $TEMP_I"
	mkdir $TEMP_I
else
	rm -rf $TEMP_I/*
fi

if [ ! -d $TEMP_O ]; then
	echo "~create $TEMP_O"
	mkdir $TEMP_O
else
	rm -rf $TEMP_O/*
fi

TEMP_FILE=$TEMP_I/tmp.txt

#step 1:read out fpga.bit from FPGA_SRC_FILE if not exist
if [ "$IMG_ALIAS" == "bitstream" ]; then
	echo "#>generate bitstream image,get fpga.bit first"
	if [ ! -f $SOURCE_FILE ]; then
		FPGA_SRC_FILE=$INPUT_DIR/BOOT-with-FPGA.BIN
		if [ ! -f $FPGA_SRC_FILE ]; then
			echo "$FPGA_SRC_FILE is not exist!"
			exit 1
		fi

		echo "########>generate $SOURCE_FILE"
		../image+ --readval -i $FPGA_SRC_FILE -b 0xCD4 -t int -o $TEMP_FILE
		read OFFSET < $TEMP_FILE
		../image+ --readval -i $FPGA_SRC_FILE -b 0xCC4 -t int -o $TEMP_FILE
		read SIZE < $TEMP_FILE

		../image+ --read2file -i $FPGA_SRC_FILE -b $OFFSET -s $SIZE -W -o $SOURCE_FILE
		echo "$>read $SIZE[W] from $FPGA_SRC_FILE offset $OFFSET[W], output=$SOURCE_FILE"
		echo "...done,file=$SOURCE_FILE"
		echo ""
		echo ""
	fi
fi

#step 2:create image header config file
BH_CFG=$TEMP_I/${IMG_ALIAS}_header.cfg
BLOCK0_ADDR=$(awk 'BEGIN{printf("0x%08X", 0 + '$HEADER_SIZE')}')
BLOCK1_ADDR=$(awk 'BEGIN{printf("0x%08X", '$BLOCK0_ADDR' + '$BLOCK_SIZE' + '$RESERV0_SIZE')}')
RECOVERY_ADDR=$(awk 'BEGIN{printf("0x%08X", '$BLOCK1_ADDR' + '$BLOCK_SIZE' + '$RESERV1_SIZE')}')
BLOCK_INFO_OFFSET=$(awk 'BEGIN{printf("0x%08X", '$BLOCK_SIZE' - 0X40)}')
echo "########>create image header config file"
echo "# image+ config file syntax:" > $BH_CFG
echo "# offset, file,      size, /path/fname, [pad_value]" >> $BH_CFG
echo "# offset, data,      size, W0, W1, W2, ...Wn" >> $BH_CFG
echo "# offset, padding,   size, padding value" >> $BH_CFG
echo "# offset, crc32,     size, start_addr, end_addr" >> $BH_CFG
echo "# offset, crc16,     size, start_addr, end_addr" >> $BH_CFG
echo "# offset, rchecksum, size, start_addr, end_addr" >> $BH_CFG
echo "#@!/image+/config" >> $BH_CFG
echo "0x00000000, data, 4,   $HEADER_MAGIC, 0xFFFFFFF0, $BLOCK0_ADDR, $BLOCK1_ADDR" >> $BH_CFG
echo "0x00000010, data, 3,   $RECOVERY_ADDR, $BLOCK_INFO_OFFSET, $BLOCK_SIZE" >> $BH_CFG
echo "0x0000001C, rchecksum, 2,          0x00000008, 0x0000001B" >> $BH_CFG
echo "0x00000020, padding,   56,         0xFFFFFFFF" >> $BH_CFG
echo "#@end" >> $BH_CFG
echo "...done,file=$BH_CFG"
echo ""
echo ""

#step 3:create block body config file
BB_CFG=$TEMP_I/${IMG_ALIAS}_body.cfg
echo "########>create block body configuration file"
../image+ --filesize -i $SOURCE_FILE -H -o $TEMP_FILE
read FSIZE < $TEMP_FILE

BODY_SIZE=$(awk 'BEGIN{printf("0x%08X", '$BLOCK_SIZE' - 0x40)}')
ADDR_C0=$BODY_SIZE
ADDR_D0=$(awk 'BEGIN{printf("0x%08X", '$ADDR_C0' + 0x10)}')
ADDR_E0=$(awk 'BEGIN{printf("0x%08X", '$ADDR_D0' + 0x10)}')
CRC32_END=$(awk 'BEGIN{printf("0x%08X", '$BLOCK_SIZE' - 0x20 - 1)}')
echo "body_size=$BODY_SIZE"
echo "# image+ config file syntax:" > $BB_CFG
echo "# offset, file,      size, /path/fname, [pad_value]" >> $BB_CFG
echo "# offset, data,      size, W0, W1, W2, ...Wn" >> $BB_CFG
echo "# offset, padding,   size, padding value" >> $BB_CFG
echo "# offset, crc32,     size, start_addr, end_addr" >> $BB_CFG
echo "# offset, crc16,     size, start_addr, end_addr" >> $BB_CFG
echo "# offset, rchecksum, size, start_addr, end_addr" >> $BB_CFG
echo "#@!/image+/config" >> $BB_CFG
echo "0x00000000, file,    $BODY_SIZE, $SOURCE_FILE, 0xFF" >> $BB_CFG
echo "$ADDR_C0, data,    4,          $FSIZE, 0x00000001, 0xFFFFFFFF, 0xFFFFFFFF" >> $BB_CFG
echo "$ADDR_D0, padding, 4,          0xFFFFFFFF" >> $BB_CFG
echo "$ADDR_E0, crc32,   8,          0x00000000, $CRC32_END" >> $BB_CFG
echo "#@end" >> $BB_CFG
echo "...done,file=$BB_CFG"
echo ""
echo ""

#step 4:create image header
BH_FILE=$TEMP_O/${IMG_ALIAS}_header.bin
echo "########>create image header block"
../image+ --create -C $BH_CFG -s $HEADER_SIZE -p 0xFF -o $BH_FILE
echo "...done,file=$BH_FILE"
echo ""
echo ""

#step 5:create image block0
BLOCK0_FILE=$TEMP_O/${IMG_ALIAS}_block0.bin
echo "########>creat image body block0"
../image+ --create -C $BB_CFG -s $BLOCK_SIZE -p 0xFF -o $BLOCK0_FILE
echo "...done,file=$BLOCK0_FILE"
echo ""
echo ""

#step 6:create image block1
BLOCK1_FILE=$TEMP_O/${IMG_ALIAS}_block1.bin
echo "########>creat image body block1"
../image+ --create -C $BB_CFG -s $BLOCK_SIZE -p 0xFF -o $BLOCK1_FILE
echo "...done,file=$BLOCK1_FILE"
echo ""

#step 7:create reserved blocks
RESERVED_0=$TEMP_O/reserved_${RESERV0_SIZE}B.bin
RESERVED_1=$TEMP_O/reserved_${RESERV1_SIZE}B.bin
echo "########>create reserved blocks"
../image+ --create -s $RESERV0_SIZE -p 0xFF -o $RESERVED_0
../image+ --create -s $RESERV1_SIZE -p 0xFF -o $RESERVED_1
echo "...done,file=$RESERVED_0 $RESERVED_1"
echo ""
echo ""

#step 7:combine the final image
FINAL_TARGET=$OUTPUT_DIR/$TARGET_NAME
echo "########>combine the final image"
../image+ --combine -i $BH_FILE \
		    -i $BLOCK0_FILE \
		    -i $RESERVED_0 \
		    -i $BLOCK1_FILE \
		    -i $RESERVED_1 \
		    -o $FINAL_TARGET

