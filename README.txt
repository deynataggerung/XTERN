Location of Files:

My code for analyzing the data can be found split between data.ipynb and analyze.ipynb. The data file reads in the data, organizes it into my data structures and runs some initial analysis on the numbers. The second file analysis mostly consists of commented out sections of code that I used to generate graphs once. It also has my code for creating a master list of locations across all users. The files can be run through jupyter without any arguments

data.txt contains the numbers from my initial analysis on every user and the locations they frequent. The data is rather and extensive and not very condensed. I left it in that state because after an initial analysis it really didn't turn out to be very useful. I included it in my report anyways as a point of interest.

the plots folder contains the plots I used to visualize data. The first 100 plots are the individualized location maps of each user. At the end I have two versions of the combined map. allgraph.png simply graphs every point from the 100 all together whereas all_locations just graphs one point for each location I found. The avg_times_hist graphs show a histogram of how many people are at each location and when.

My analysis of the data I found is in the report.docx and report.pdf files. This summarizes what I noticed and how I think it can be used.

Notes on Methodology:
The first thing to note is that I copied the entire header section into both of the code files. I would have just imported these from myclasses and vastly simplified the code but I was having issues with jupyter not properly updating the import whenever I made changes to the classes.

I have been unfortunately pressed for time on finishing this report due to an oversight on my part so there were a couple of things I didn't quite get to but was aware of. I mentioned in my report that it's possible that each person had fairly regular patterns that just shifted between weekdays and weekends. I would have liked to implement a way to sort out weekday times and weekend times to try and find a pattern for when a person would be in a certain place. It's possible though that due to the way the data was generated this pattern doesn't actually exist.

I also have an issue on the way I decide the clustering for what defines a location. I couldn't use k-means because I don't know how many locations each person has and didn't want to limit that and get strange clusters. The way I did it is fairly simple and assumes that clusters are fairly close together and far apart from each other. Specifically the far apart from each other was a problem where if there was a cluster inbetween two other clusters (around 1,0.8) it got incorporated half and half into those two clusters. This wasn't as big a deal in my opinion since a number of different locations in one area can often be categorized together as a shopping mall or campus.

I hope that despite the shortcomings I showed that I can bring together data to find results and that with more experience and time I will be capable of creating a polished final product.
