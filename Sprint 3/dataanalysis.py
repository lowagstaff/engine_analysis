import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")

#Questions:
# Are all the engine pressures related? 
# Does higher RPM cause engine failure? 

print("Information about data: 0 = Bad engine condition, 1 = Good engine condition\n")

#Read in CSV
#df = pd.read_csv(r"C:\Users\wagst\Documents\BYU-I\BYU-I Spring 2024\Applied Programming\Programs\Sprint 3\engine_data.csv")
df = pd.read_csv("engine_data.csv")

#Sort the values for engine condition and rpm
df = df.sort_values(['Engine Condition', 'Engine rpm'])

#Set index to RPM to compare across dataset
df = df.set_index('Engine rpm')

#Print dataframe
print(df)
#Find calculations for lube pressures:
lubepressures = df.groupby('Engine rpm').agg({'Lub oil pressure': ['mean', 'min', 'max']})
lubepressuresdata = df.groupby('Engine Condition').agg({'Lub oil pressure': ['mean', 'min', 'max']})


#Results and graphs
print(lubepressures)
lubepressures.plot.bar()
plt.locator_params(axis='x', nbins=25)
plt.xlim(60, 2300)
plt.show()

print(lubepressuresdata)
lubepressuresdata.plot.bar()
plt.locator_params(axis='x', nbins=25)
plt.show()


#Ask user for input to move to next section:
print("\nWhat are your thoughts about this data? ")
print("Do you think the data is related to engine failure?\n")

input("\nPress enter to continue:")

#Move to next dataset: fuel pressure:
fuelpressures = df.groupby('Engine rpm').agg({'Fuel pressure': ['mean', 'min', 'max']})
fuelpressuresdata = df.groupby('Engine Condition').agg({'Fuel pressure': ['mean', 'min', 'max']})

#Results and graphs
print(fuelpressures)
fuelpressures.plot.bar()
plt.locator_params(axis='x', nbins=25)
plt.xlim(60, 2300)
plt.show()

print(fuelpressuresdata)
fuelpressuresdata.plot.bar()
plt.locator_params(axis='x', nbins=25)
plt.show()

#Ask user for input to move to next section:
print("\nWhat are your thoughts about this data? ")
print("Do you think the data is related to engine failure?\n")

input("\nPress enter to continue:")

#Move to next dataset: coolant pressure:
coolpressures = df.groupby('Engine rpm').agg({'Coolant pressure': ['mean', 'min', 'max']})
coolpressuresdata = df.groupby('Engine Condition').agg({'Coolant pressure': ['mean', 'min', 'max']})

#Results and graphs
print(coolpressures)
coolpressures.plot.bar()
plt.locator_params(axis='x', nbins=25)
plt.xlim(60, 2300)
plt.show()

print(coolpressuresdata)
coolpressuresdata.plot.bar()
plt.locator_params(axis='x', nbins=25)
plt.show()

#Ask user for input to move to next section:
print("\nWhat are your thoughts about this data? ")
print("Do you think the data is related to engine failure?\n")

input("\nPress enter to continue:")

#Move to next dataset: lube oil temp:
lubetemp = df.groupby('Engine rpm').agg({'lub oil temp': ['mean', 'min', 'max']})
lubetempdata = df.groupby('Engine Condition').agg({'lub oil temp': ['mean', 'min', 'max']})

#Results and graphs
print(lubetemp)
lubetemp.plot.bar()
plt.locator_params(axis='x', nbins=25)
plt.xlim(60, 2300)
plt.show()

print(lubetempdata)
lubetempdata.plot.bar()
plt.locator_params(axis='x', nbins=25)
plt.show()

#Ask user for input to move to next section:
print("\nWhat are your thoughts about this data? ")
print("Do you think the data is related to engine failure?\n")

input("\nPress enter to continue:")

#Move to next dataset: Coolant Temp:
cooltemp = df.groupby('Engine rpm').agg({'Coolant temp': ['mean', 'min', 'max']})
cooltempdata = df.groupby('Engine Condition').agg({'Coolant temp': ['mean', 'min', 'max']})

#Results and graphs
print(cooltemp)
cooltemp.plot.bar()
plt.locator_params(axis='x', nbins=25)
plt.xlim(60, 2300)
plt.show()

print(cooltempdata)
coolplot = cooltempdata.plot.bar()
plt.locator_params(axis='x', nbins=25)
plt.show()

#Ask user for input to move to next section:
print("\nWhat are your thoughts about this data? ")
print("Do you think the data is related to engine failure?\n")

input("\nPress enter to continue:")


#Move to next dataset: Engine RPM:
rpm = df.groupby('Engine rpm').agg({'Engine Condition': ['mean']})

print("This graph will take the average amounts of 0's and 1's \ntherefore the higher the average the better the engines, the lower the average the worse the engines.")

#Results and graphs
print(rpm)
rpm.plot.bar()
plt.locator_params(axis='x', nbins=25)
plt.xlim(60, 2300)
plt.show()

#Ask user for input to move to next section:
print("\nWhat are your thoughts about this data? ")
print("Do you think the data is related to engine failure?\n")


print("Question1: Are all the engine pressures related? ")
print("I believe so, most of the time the pressures look similar; especially in terms of engine performance:\n")

print("Question2: Does higher RPM cause engine failure?")
print("From the data, it looks like engine RPM does account for engine failure, we can see the higher RPM the average goes down towards 0")

print("\nData analysis complete. Goodbye!\n")

