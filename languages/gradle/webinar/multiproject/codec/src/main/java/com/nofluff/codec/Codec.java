package com.nofluff.codec;

import java.util.ArrayList;
import java.util.List;
import org.apache.commons.codec.binary.Base64;

public class Codec {  
  public String encode(String text) {
    Base64 codec = new Base64();
    return new String(codec.encode(text.getBytes()));
  }
}
