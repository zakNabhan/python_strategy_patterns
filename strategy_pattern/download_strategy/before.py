'''
this example for download video
'''


def video_format(strategy=None) -> str:

    if strategy == "HD":
        print(f"Downloading Video in {strategy}")
    elif strategy == "normal":
        print(f"Downloading Video in {strategy} quality")
    else:
        print("Strategy not implemented...")


def main():
    video_format("hd")
    video_format("HD")


if __name__ == "__main__":
    print("Select Video Format")
    main()
