package com.jollen.util;

class Demo {
    public String getInfo() {
        return "#>Package info.";
    }
}

public class Demo26Package {
    public static void main(String[] args) {
        Demo d = new Demo();
        System.out.println(d.getInfo());
    }
}
