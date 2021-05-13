import comment_extract as CE
import sentimentYouTube as SYT

def main():
    
	# EXAMPLE VideoId = 'tCXGJQYZ9JA'
	videoId = input("Enter id: ")
	# Fetch the number of comments
	# if count = -1, fetch all comments
	count = int(input("Enter No of Comments :"))
	comments = CE.commentExtract(videoId, count)
    
	SYT.sentiment(comments)


if __name__ == '__main__':
	main()
