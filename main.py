# python 3.7.x
# Pulls top n wallpapers and places them into directory

DIRECTORY = "wallpapers" # where we'll store the wallpapers
count = 30 # How many wall papers we want

SUBREDDIT = "wallpapers"

def reddit_get_top_posts(limit, subreddit):
	url = f"https://reddit.com/{SUBREDDIT}"

	while limit > 0:


	pass


def reddit_extract_image_sources():
	pass


def download_images(image_sources):
	"""
	params:
		image_sources [<strings>]: list of urls with images

	"""
	pass


def validate_image(image):
	"""
	Validates quality of image is acceptable
	params:
		image ?
	"""
	pass



def main():
	pass


if __name__ == "__main__":
	main()
