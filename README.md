# honors-project-CLD
## Name: Padakanti Srijith
## ID.no: 2019114002
## Group: CLD
## Project: Enhancing Telugu Wikipedia
## Faculty: Radhika Mamidi

## Content Generation - Plants Domain
Machine translated Telugu wikipedia for plants
### Aim: 
The aim of this Honors project is to increase the number of Telugu wikipedia pages in any domain. The domain I chose is plants domain.
The total number of plant telugu wikipedia pages I created are 7416.

### Objectives:
1) Scraping the data for plants to create a plant database.
2) Machine translating the data into Telugu.
3) Creating a Template for wikipedia article.
4) Creating .xml for wikipedia articles.


### Related work:
1) Data Scraping from plants related websites.
2) Machine translating the plants database.
3) Prepared a database for plants using 40 attributes and 7416 types.
4) Post editing and formatiing the machine translated data.
5) Final plants database [Here](https://docs.google.com/spreadsheets/d/1lbGH9-2tr1NSMClUi_FNch0qDr9RmBPmwqZAEQ0M4oI/edit#gid=0)

### Methodology:
1) First collect the data to make a dataset.
2) Use machine translation to translate the database into telugu database.
3) Correct the telugu database after machine translation.
4) The .csv file for plants dataset. [here](https://docs.google.com/spreadsheets/d/1DUPudD23SuMjWWg8wX-OJzOoxEp-zePhNu3TuvISing/edit#gid=1216063786)
5) Use the jinja2 template to write a template for the wikipedia page.
6) Use macro for writing the template.
7) use python to create a .xml file for uploading to the sandbox.

### Experiments/Results/Discussion:
1) Collected datafor plants database.
2) Translated data into telugu.
3) Created template for article generation.
4) Created .xml file for 7416 wikipedia pages based on different plants.


### Future work:
1) Correct some mistakes in the template.
2) Translate the sentences bettter by using Deeptrans.
3) Collect image data from wiki commons.
4) Change data such that it can fit into any template so that it can be translated into different languages.
5) Add more detailed data to the plants wikipedia.
6) Upload the .xml files to wikipedia.


# Work this year:

## From the future work of last year's report:

### 1) Corrected and completed the template:
##### a) The sentences were finalisedwith the help of kasyap sir and vibha ma'am.
##### b) Infobox is added to the template.
##### c) categories are also included in the template.
##### d) The article is divided into easy to understand/search categories. This is to make it easier for the user to understand/search in the wikipedia article.
	
### 2) Translate sentences better using DEEPtrans:
##### a) Tried using Deeptrans to translate the sentences but was not satisfied by the translated result.
##### b) Then tried to translate with anuvaad only to get unsatifactory translations.
##### c) Then used bing_translate for the translation of the sentences and paragraphs but the translations were just ok and some places the translation was horrible.
##### d) Even tried all these methods by diving the paragraphs into sentences then translating them this was a little better compared to the before attempts but even so some of the sentences were not translating correctly as the intuition or the assuming words of translating tool makes the translation difficult to happen correctly.
##### e) Due to this I gave up the idea of translating the paragraphs and decided to extract the important data from the paragraphs and then make it into structured data for using as structured data is easy to use and translate into different languages at any time.
##### f) So, the data was completely converted into structure data and can be used to make into  different languages wikipedia with little effort.

### 3) Collect image data from wiki commons:
##### a) Completed collecting images and the image thumb from the wiki commons.
	
### 4) Change data such that it can fit into any template so that it can be translated into different languages:
##### a) Changed the data into structured data so with the help of transliteration and the translation of some attributes the data can fit any template.
	
### 5) Upload the .xml files to wikipedia:
##### a)Completed creating the xml dump, will have to send it to ramu sir for checking and the upload.

### 6)Addtional changes:
##### a) Transliterated many of the attributes.
##### b) Experienced many translators due to relatively less accurate translators for telugu language.
##### c) Got a grasp for extracting text, links, data.
##### d) Added infobox and categories to the template.
##### e) Extracted key words from 4 categories.
	
	
The final dataset which is strutured is [here](https://docs.google.com/spreadsheets/d/17XLbnxtIJ2C-HR3W_JOmWFt6p5gpSWzygAG8D9yTvuo/edit?usp=sharing) .

The code required to run this file can be viewed [here](https://colab.research.google.com/drive/1RNwc0WoeyY3_ooZnR56yYOWcFY4A0Ft4?usp=sharing) . 

The sample article can be viewed [here](https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%BE%E0%B0%A1%E0%B1%81%E0%B0%95%E0%B0%B0%E0%B0%BF:Srijith2002) .

### Summary:

There are 7416 plants in my plants database. Completed and finalised the database. Completed the template. Created xml files, needs to be reviewed.
