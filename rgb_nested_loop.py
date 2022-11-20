#!/usr/bin/env python3

# Created By: Nathan A
# Date: Nov. 17, 2022
# This program displays all the possible RGB colors


def main():

    for red in range(0, 1):
        for green in range(0, 1):
            for blue in range(0, 256):
                print(f"{red},{green},{blue}")


if __name__ == "__main__":
    main()
