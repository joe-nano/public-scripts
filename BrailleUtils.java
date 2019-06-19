package com.tramvm;

/**
 * Convert braille dot to text
 * By tramvm@gmail.com
 */

public class BrailleUtils {
    public static String mapDotBraille(boolean dot1, boolean dot2, boolean dot3, boolean dot4, boolean dot5, boolean dot6) {
        StringBuilder strDots = new StringBuilder();
        if (dot1){
            strDots.append("1");
        }
        if (dot2){
            strDots.append("2");
        }
        if (dot3){
            strDots.append("3");
        }
        if (dot4){
            strDots.append("4");
        }
        if (dot5){
            strDots.append("5");
        }
        if (dot6){
            strDots.append("6");
        }

        if (strDots.toString().equals("1")) {
            return "a";
        }
        if (strDots.toString().equals("12")) {
            return "b";
        }
        if (strDots.toString().equals("14")) {
            return "c";
        }
        if (strDots.toString().equals("145")) {
            return "d";
        }
        if (strDots.toString().equals("15")) {
            return "e";
        }
        if (strDots.toString().equals("124")) {
            return "f";
        }
        if (strDots.toString().equals("1245")) {
            return "g";
        }
        if (strDots.toString().equals("125")) {
            return "h";
        }
        if (strDots.toString().equals("24")) {
            return "i";
        }
        if (strDots.toString().equals("245")) {
            return "j";
        }
        if (strDots.toString().equals("13")) {
            return "k";
        }
        if (strDots.toString().equals("123")) {
            return "l";
        }
        if (strDots.toString().equals("134")) {
            return "m";
        }
        if (strDots.toString().equals("1345")) {
            return "n";
        }
        if (strDots.toString().equals("135")) {
            return "o";
        }
        if (strDots.toString().equals("1234")) {
            return "p";
        }
        if (strDots.toString().equals("12345")) {
            return "q";
        }
        if (strDots.toString().equals("1235")) {
            return "r";
        }
        if (strDots.toString().equals("234")) {
            return "s";
        }
        if (strDots.toString().equals("2345")) {
            return "t";
        }
        if (strDots.toString().equals("136")) {
            return "u";
        }
        if (strDots.toString().equals("1236")) {
            return "v";
        }
        if (strDots.toString().equals("2456")) {
            return "w";
        }
        if (strDots.toString().equals("1346")) {
            return "x";
        }
        if (strDots.toString().equals("13456")) {
            return "y";
        }
        if (strDots.toString().equals("1356")) {
            return "z";
        }

        return "";
    }
}
