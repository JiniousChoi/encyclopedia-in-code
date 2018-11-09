package org.gradle.poetry;

import java.util.ArrayList;
import java.util.List;

public class Poetry {
    
    public List<String> makeList() {
        List<String> ls = new ArrayList();
        ls.add("This is line #1");
        ls.add("This is line #2");
        ls.add("This is line #3");
        ls.add("This is line #4");
        ls.add("This is line #5");
        return ls;
    }

    public void emit(List<String> lines) {
        for (String line : lines) {
            System.out.println(line);
        }
    }

    public static void main(String[] args) {
        Poetry p = new Poetry();
        p.emit(p.makeList());
    }

}
