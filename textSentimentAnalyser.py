#It's a tool which can be used to analyse 
#the sentiment of a text on a website whether it's positive or
#negative.
 
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

def printReviews(reviews):
	for review in reviews:
		print(review)
		
def findSentiment(text):
	sentiment = TextBlob(text).sentiment.polarity
	return sentiment

def main():
	url = input("Enter URL of the website: ")

	htmlPage = requests.get(url)

	try:
		htmlPage.raise_for_status()
		
		soup = BeautifulSoup(htmlPage.text,"html.parser")

		reviews = soup.find_all('p')
		
		positiveReviews = 0
		negativeReviews = 0
		neutralReviews = 0
		positiveList = []
		neutralList = []
		negativeList = []
		for review in reviews:
			text = review.get_text()
			sentiment = findSentiment(text)
			if(sentiment > 0):
				positiveReviews += 1
				positiveList.append(text)
			elif(sentiment == 0):
				neutralReviews += 1
				neutralList.append(text)
			else:
				negativeReviews += 1
				negativeList.append(text)
				
		if(positiveReviews > 0):
			print("\n*****These are positive reviews.:)*****\n")
			printReviews(positiveList)
			print("\nTotal positive reviews: ",str(positiveReviews)+'\n')
			
		if(neutralReviews > 0):
			print("\n*****These are neutral reviews.:)*****\n")
			printReviews(neutralList)
			print("\nTotal neutral reviews: ",str(neutralReviews)+'\n')
			
		if(negativeReviews > 0):
			print("\n*****These are negative reviews.*****\n")
			printReviews(negativeList)
			print("\nTotal negative reviews: ",str(negativeReviews)+'\n')

	except Exception as exc:
		print("There was a problem: %s" %(exc))
	
if __name__ == "__main__" :
	main()
