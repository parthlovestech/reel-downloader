import instaloader

def download_reel(url):
    # Create an Instaloader object
    L = instaloader.Instaloader()

    # Extract the shortcode from the URL
    shortcode = url.split('/')[-2]

    try:
        # Download the reel
        L.download_post(instaloader.Post.from_shortcode(L.context, shortcode), target='reels')
        print(f"Reel downloaded and saved in 'reels' directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    instagram_url = input("Enter the Instagram Reel URL: ")
    download_reel(instagram_url)