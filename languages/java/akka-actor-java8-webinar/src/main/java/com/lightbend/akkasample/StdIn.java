/*
 * Copyright (C) 2016 Lightbend Inc. <http://www.lightbend.com>
 */
package com.lightbend.akkasample;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class StdIn {

  public static String readLine() {
    // written to make it work in intellij as System.console() is null
    // when run inside the IDE
    try {
      //Console
      //java.io.Console console = System.console();
      //System.out.println("console: " + console);
      //return console.readLine();
      
      //Scanner
      //java.util.Scanner scanner = new java.util.Scanner(System.in);
      //System.out.println(scanner);
      //return scanner.nextLine();
    
      return new BufferedReader(new InputStreamReader(System.in)).readLine();
    } catch (Exception ex) {
      throw new RuntimeException(ex);
    }
  }
}
