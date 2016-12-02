package com.jollen.util.b;

import com.jollen.util.a.HelloDemo;

class SubHelloDemo extends HelloDemo {
    public void printInfo() {
        System.out.println("#>Access protected content:" + super.name);
    }
}

public class Demo27Protected {
    public static void main(String[] args) {
        new SubHelloDemo().printInfo();
    }
}
