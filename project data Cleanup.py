import csv
with open("project_1.csv", "r") as file:
	data=csv.reader(file)
	header=next(data)
	header=[column.strip().lower() for column in header]
	count={}
	records=[]
	for column in header:
		count[column] ={}
	for row in data:
		record={}
		for x in range(len(header)):
			column=header[x]
			value=row[x]
			record[column]=value
			if value not in count[column]:
				count[column][value]=1
			else:
				count[column][value]+=1
		records.append(record)
total={}
for column in header:
	total[column]={}
	for value,freq in count[column].items():
		try:
			number=int(value)
			total[column][number]=number*freq
		except ValueError:
			continue
print("Q1. Whats the average number of children?\nA.", sum(total["children"].values())/sum(count["children"].values()))
print("Q2.Whats the average household count?\nA.",sum(total["household_size"].values())/sum(count["household_size"].values()))		
region_data = {}
for record in records:
    region = record["region"]
    children = int(record["children"])
    if region not in region_data:
    	region_data[region] = [0, 0]
    region_data[region][0] += children
    region_data[region][1] += 1
print("Q3. How does average number of children vary by region?.\nA.")
highest_children=0
highest_name=""
lowest_children=999999999
lowest_name=""
for region in region_data:
	region_total,region_count=region_data[region]
	avg=region_total/region_count
	if avg>highest_children:
		highest_children=avg
		highest_name=region
	if avg<lowest_children:
		lowest_children=avg
		lowest_name=region
	print(region,":",round(avg,2))
print("Q4.Which region has the highest and Lowest number of children?\nA.")
print("Highest Average Children",":",highest_name,"with",round(highest_children,2))
print("lowest Average Children",":",(lowest_name),"with",round(lowest_children,2))
def group_by_column(records,group_column):
	grouped={}
	for record in records:
		key=record[group_column]
		children=int(record["children"])
		household_size=int(record["household_size"])
		if key not in grouped:
			grouped[key]=[0,0,0]
		grouped[key][0]+=children
		grouped[key][1]+=household_size
		grouped[key][2]+=1
	return grouped
education_data=group_by_column(records,"education")
employment_data=group_by_column(records,"employment")
print("Q5. How do education groups differ in their average number of children And Household size")
for education in education_data:
	total_children,total_household,count=education_data[education]
	avg_children=total_children/count
	avg_household=total_household/count
	print(education,": avg children=",round(avg_children,2),", Avg household=",round(avg_household,2))
print("Q6.How do employment groups differ in the average number of children and household size?\nA.")
for employment in employment_data:
	total_children,total_household,count=employment_data[employment]
	avg_children=total_children/count
	avg_household=total_household/count
	print(employment,"avg children=",round(avg_children,2),",avg household=",round(avg_household,2))