import numpy as np
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

g_SAMPLE_SIZE = 150


def genderDistributions():
  # Mapping for Genders
  '''
  0 -> Prefer Not Say
  1 -> Male
  2 -> Female
  3 -> Other
  '''

  maleCount = 0
  femaleCount = 0
  otherCount = 0
  preferNotSayCount = 0

  preferNotSayIndex = 0
  maleIndex = 1
  femaleIndex = 2
  otherIndex = 3

  print("Running Function for Gender DataSet")
  # genders = np.round(np.random.uniform(0, 3, size=g_SAMPLE_SIZE))
  genders = np.round(np.random.normal(loc=1.5, scale=0.5, size=g_SAMPLE_SIZE))
  for _ in genders:
    if _ == maleIndex:
      maleCount += 1
    elif _ == femaleIndex:
      femaleCount += 1
    elif _ == otherIndex:
      otherCount += 1
    elif _ == preferNotSayIndex:
      preferNotSayCount += 1

  x_axis = ["Males", "Females", "Others", "Prefer Not Say"]
  y_axis = np.array([maleCount, femaleCount, otherCount, preferNotSayCount])

  fig, ax = plt.subplots(figsize=(16, 9))
  ax.barh(x_axis, y_axis)
  ax.set_title("Distribution of Responses Based on Gender")
  ax.invert_yaxis()

  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)

  for _ in ax.patches:
    plt.text(_.get_width()+0.2, _.get_y()+0.4, str(_.get_width()))

  plt.show()

def toolDistribution():
  print("Starting the function for tool Distribution")

  # Mapping for Tools
  '''
  Splunk -> 0
  ERP Softwares -> 1
  CRM Tools -> 2
  Other -> 3
  '''

  splunkIndex = 0
  ERPIndex = 1
  CRMIndex = 2
  otherIndex = 3

  splunkCount = 0
  ERPCount = 0
  CRMCount = 0
  otherCount = 0

  tools = np.round(np.random.normal(loc=1.0, scale=0.5, size=g_SAMPLE_SIZE))
  for _ in tools:
    if _ == splunkIndex:
      splunkCount += 1
    elif _ == ERPIndex:
      ERPCount += 1
    elif _ == CRMIndex:
      CRMCount += 1
    elif _ == otherIndex:
      otherCount += 1

  x_axis = ["Splunk", "ERP Softwares", "CRM Tools", "Other"]
  y_axis = np.array([splunkCount, ERPCount, CRMCount, otherCount])

  fig, ax = plt.subplots(figsize=(16, 9))
  ax.barh(x_axis, y_axis)
  ax.set_title("Distribution of Responses Based on Tools")
  ax.invert_yaxis()

  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)

  for _ in ax.patches:
    plt.text(_.get_width()+0.2, _.get_y()+0.4, str(_.get_width()))

  plt.show()


def programFrequency():
  print("Starting Function for program Frequency")

  # Mapping for Program Frequency
  '''
  Monthly -> 0
  Quarterly -> 1
  Annual -> 2
  More Often -> 3

  '''

  monthlyIndex = 0
  quarterlyIndex = 1
  annuallyIndex = 2
  moreIndex = 3

  monthlyCount = 0
  quarterlyCount = 0
  annuallyCount = 0
  moreCount = 0

  programs = np.round(np.random.normal(loc=1.25, scale=0.5, size=g_SAMPLE_SIZE))
  for _ in programs:
    if _ == monthlyIndex:
      monthlyCount += 1
    elif _ == quarterlyIndex:
      quarterlyCount += 1
    elif _ == annuallyIndex:
      annuallyCount += 1
    elif _ == moreIndex:
      moreCount += 1
  
  x_axis = ["Monthly", "Quarterly", "Annually", "More-Often"]
  y_axis = np.array([monthlyCount, quarterlyCount, annuallyCount, moreCount])

  fig, ax = plt.subplots(figsize=(16, 9))
  ax.barh(x_axis, y_axis)
  ax.set_title("Frequency of Awareness Programs")
  ax.invert_yaxis()

  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)

  for _ in ax.patches:
    plt.text(_.get_width()+0.2, _.get_y()+0.4, str(_.get_width()))
     
  plt.show()

def ageDistribution():
  print("Starting the function for Age Distribution")
  
  # Mapping for Age Distribution
  '''
  < 10 -> 0
  10 - 20 -> 1
  20 - 30 -> 2
  30 - 40 -> 3
  40 - 50 -> 4
  50 - 60 -> 5
  60 - 70 -> 6
  > 70 -> 7
  '''

  bTenIndex = 0
  tenTwentyIndex = 1
  twentyThirtyIndex = 2
  thirtyFourtyIndex = 3
  fourtyFiftyIndex = 4 
  fiftySixtyIndex = 5
  sixtySeventyIndex = 6 
  aSeventyIndex = 7


  bTenCount = 0
  tenTwentyCount = 0
  twentyThirtyCount = 0
  thirtyFourtyCount = 0
  fourtyFiftyCount = 0
  fiftySixtyCount = 0
  sixtySeventyCount = 0
  aSeventyCount = 0

  ages = np.round(np.random.normal(loc=2.5, scale=1.0, size=g_SAMPLE_SIZE))
  for _ in ages:
    if _ == bTenIndex:
      bTenCount += 1
    elif _ == tenTwentyIndex:
      tenTwentyCount += 1
    elif _ == twentyThirtyIndex:
      twentyThirtyCount += 1
    elif _ == thirtyFourtyIndex:
      thirtyFourtyCount += 1
    elif _ == fourtyFiftyIndex:
      fourtyFiftyCount += 1
    elif _ == fiftySixtyIndex:
      fiftySixtyCount += 1
    elif _ == sixtySeventyIndex:
      sixtySeventyCount += 1
    elif _ == aSeventyIndex:
      aSeventyCount += 1
  x_axis = [" < 10", "10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "> 70"]
  y_axis = np.array([bTenCount, tenTwentyCount, twentyThirtyCount, thirtyFourtyCount, fourtyFiftyCount, fiftySixtyCount, sixtySeventyCount, aSeventyCount])

  fig, ax = plt.subplots(figsize=(16, 9))
  ax.barh(x_axis, y_axis)
  ax.set_title("Age Distribution of Responses")
  ax.invert_yaxis()

  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)

  for _ in ax.patches:
    plt.text(_.get_width()+0.2, _.get_y()+0.4, str(_.get_width()))
  plt.show()

if __name__ == '__main__':
  # genderDistributions()
  # toolDistribution()
  programFrequency()
  # ageDistribution()