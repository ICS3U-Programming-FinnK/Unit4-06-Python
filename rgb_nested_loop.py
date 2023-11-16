#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: November 16th, 2023
#


def main() -> None:
    # Loop for red (r) values
    for r in range(256):
        # Loop for green (g) values
        for g in range(256):
            # Loop for blue (b) values
            for b in range(256):
                # Print the RGB color code and change the color of the output
                print(f"\033[38;2;{r};{g};{b}mRGB({r}, {g}, {b})\033[0m")


if __name__ == "__main__":
    main()
