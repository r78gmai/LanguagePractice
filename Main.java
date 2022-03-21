package com.company;

import javax.sound.midi.SysexMessage;

// 抽象クラス
abstract class Animal {
    abstract void call();
}

class Dog extends Animal {
    public void call() {
        System.out.println("Won!");
    }
}
class Cat extends Animal {
    public void call() {
        System.out.println("Nyan!");
    }
}
class Someone {
    Someone (Animal animal) {
        // 受け取ったオブジェクトのcall メソッドを呼ぶ
        animal.call();
    }
}

public class Main {

    public static void main(String[] args) {
	// write your code here
        System.out.println("Java");

        // 継承 → ポリモーフィズム
        new Someone( new Dog() ); //won
        // call の実装が切り替わる
        new Someone( new Cat() ); //cat
    }
}
