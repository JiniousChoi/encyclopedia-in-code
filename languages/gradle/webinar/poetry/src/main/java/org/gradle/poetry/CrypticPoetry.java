package org.gradle.poetry;

import java.util.List;
import org.apache.commons.codec.binary.Base64;

public class CrypticPoetry {
    
    public static void crypticEmit(List<String> lines) {
        for (String line : lines) {
            System.out.println(encode(line));
        }
    }

    public static String encode(String text) {
        Base64 codec = new Base64();
        return new String(codec.encode(text.getBytes()));
    }

    public static void main(String[] args) {
        Poetry p = new Poetry();
        crypticEmit(p.makeList());
    }

}
