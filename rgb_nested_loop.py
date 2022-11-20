#!/usr/bin/env python3

# Created By: Nathan A
# Date: Nov. 17, 2022
# This program displays all the possible RGB colors


def main():

    # for loop to determine the red ID
    for red in range(0, 1):
        # for loop to determine the green ID
        for green in range(0, 1):
            # for loop to determine blue red ID
            for blue in range(0, 256):
                print(f"{red},{green},{blue}")


if __name__ == "__main__":
    main()
