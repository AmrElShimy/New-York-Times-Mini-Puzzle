
import java.awt.*;
import java.util.ArrayList;

import javax.swing.*;

public class Grid extends JPanel {

    public void paint(Graphics g) {
        getData hints = new getData();
        ArrayList<String> numbers = new ArrayList<String>();
        System.out.println(hints.readHints());
        for (int i = 0; i < 5; i++) {

            for (int k = 0; k < 5; k++) {
                g.drawRect((40 + (k * 60)), (140 + (i * 60)), 60, 60);
                g.setColor(Color.black);

                if (Character.isDigit(hints.readText().get((i * 5) + k + 10)
                        .charAt(hints.readText().get((i * 5) + k + 10).length() - 1))) {
                    g.setFont(new Font("default", Font.BOLD, 10));
                    g.drawString(
                            Character.toString(hints.readText().get((i * 5) + k + 10)
                                    .charAt(hints.readText().get((i * 5) + k + 10).length() - 1)),
                            (40 + (k * 60)) + 5, (140 + (i * 60)) + 15);
                    g.setFont(new Font("default", Font.BOLD, 38));
                    g.drawString(
                            Character.toString(hints.readText().get((i * 5) + k + 10)
                                    .charAt(hints.readText().get((i * 5) + k + 10).length() - 3)),
                            (40 + (k * 60)) + 20, (147 + (i * 60)) + 35);
                } else {

                    g.drawString(
                            Character.toString(hints.readText().get((i * 5) + k + 10)
                                    .charAt(hints.readText().get((i * 5) + k + 10).length() - 1)),
                            (35 + (k * 60)) + 20, (148 + (i * 60)) + 35);
                    if (hints.readText().get((i * 5) + k + 10)
                            .charAt(hints.readText().get((i * 5) + k + 10).length() - 1) == 'k') {
                        g.fillRect((40 + (k * 60)), (140 + (i * 60)), 60, 60);

                    }
                }
            }

        }
        g.setFont(new Font("default", Font.BOLD, 16));

        g.drawString("ACROSS", 420, 80);
        g.setFont(new Font("default", Font.PLAIN, 16));
        //System.out.println(hints.readHints());
        for (int i = 0; i < 5; i++) {
            g.drawString(hints.readText().get(i), 420, (100 + (i * 20)));
            numbers.add(Character.toString(hints.readText().get(i).charAt(0)) + ". ");
        }
        g.setFont(new Font("default", Font.BOLD, 16));
        g.drawString("DOWN", 420, 220);
        for (int i = 5; i < 10; i++) {
            g.setFont(new Font("default", Font.PLAIN, 16));
            g.drawString(hints.readText().get(i), 420, (240 + ((i - 5) * 20)));
            numbers.add(Character. toString(hints.readText().get(i).charAt(0)) + ". ");
        }
        g.setFont(new Font("default", Font.BOLD, 16));
        g.drawString("NEW ACROSS", 420, 360);
        g.setFont(new Font("default", Font.PLAIN, 16));
        for (int i = 0; i < 5; i++) {
            //System.out.println(hints.readHints().size());//.substring(5, hints.readHints().get(i).length()));
            g.drawString(" " + hints.readHints().get(i), 429,
                    (380 + (i * 20)));
            g.drawString(numbers.get(i),420,(380 + (i * 20)));
        }
        System.out.println(numbers);
        g.setFont(new Font("default", Font.BOLD, 16));
        g.drawString("NEW DOWN", 420, 500);
        g.setFont(new Font("default", Font.PLAIN, 16));
        if (hints.readHints().get(0).charAt(1) == ' ') {
            if (hints.readHints().get(0).charAt(2) != ' ') {
                if (hints.readHints().get(0).charAt(3) != ' ') {
                    for (int i = 6; i < 10; i++) {

                        g.drawString(hints.readHints().get(i), 429,
                                (520 + ((i - 6) * 20)));
                        g.drawString(numbers.get(i-1),420,(520 + ((i-6) * 20)));
                    }
                    g.drawString(hints.readHints().get(5).substring(5, hints.readHints().get(5).length()), 429,
                            (520 + (4 * 20)));
                    g.drawString(numbers.get(9),420,520 + (4 * 20));
                } else
                {

                    for (int i = 6; i < 9; i++) {
                        g.drawString(hints.readHints().get(i).substring(5, hints.readHints().get(i).length()), 429,
                                (520 + ((i - 6) * 20)));
                        g.drawString(numbers.get(i-1),420,(520 + ((i-6) * 20)));}

                    g.drawString(hints.readHints().get(5).substring(5, hints.readHints().get(5).length()), 429,
                            (520 + ((3) * 20)));
                    g.drawString(numbers.get(8),420,(520 + (3 * 20)));
                    g.drawString(hints.readHints().get(9).substring(5, hints.readHints().get(9).length()), 429,
                            (520 + (4 * 20)));
                    g.drawString(numbers.get(9),420,(520 + (4 * 20)));

                }
            }

            else {
                for (int i = 7; i < 10; i++) {
                    g.drawString(hints.readHints().get(i).substring(5, hints.readHints().get(i).length()), 420,
                            (520 + ((i - 7) * 20)));
                }
                g.drawString(hints.readHints().get(5).substring(5, hints.readHints().get(5).length()), 420,
                        (520 + ((3) * 20)));
                g.drawString(hints.readHints().get(6).substring(5, hints.readHints().get(6).length()), 420,
                        (520 + (4 * 20)));
            }
        } else {
            for (int i = 5; i < 10; i++) {
                g.drawString(hints.readHints().get(i).substring(0, hints.readHints().get(i).length()), 435,
                        (520 + ((i - 5) * 20)));
            }
            for (int i = 5; i < 10; i++) {
                g.drawString(numbers.get(i),420,(520 + ((i-5) * 20)));
            }

        }

        g.drawString(hints.date1, 180, 470);
        g.drawString("PUZZLE DATE: ", 70, 470);

        System.out.println();
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("PL Project");

        frame.add(new Grid());
        frame.setSize(1400, 750);
        frame.setVisible(true);
        frame.setBackground(Color.white);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setResizable(false);
    }

}
