# !pip install soccernet
from SoccerNet.Downloader import SoccerNetDownloader

def main(base_dir="data/SoccerNet"):
    downloader = SoccerNetDownloader(LocalDirectory=base_dir)
    downloader.password = "s0cc3rn3t"
    # Download development kit per task
    downloader.downloadDataTask(
        task="tracking-2023", split=["train", "valid", "challenge"]
    )

if __name__ == "__main__":
    main()