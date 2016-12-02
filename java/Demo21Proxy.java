interface Network {
    public void browse();
}

class Real implements Network {
    public void browse() {
        System.out.println("$$$$>Browse Infomation on Network.");
    }
}

class Proxy implements Network {
    private Network network;

    public Proxy(Network network) {
        this.network = network;
    }

    public void check() {
        System.out.println("$$$$>Chcek network");
    }

    public void browse() {
        this.check();
        this.network.browse();
    }
}

public class Demo21Proxy {
    public static void main(String[] args) {
        Network net = new Real();
        Proxy p = new Proxy(net);

        p.browse();
    }
}

