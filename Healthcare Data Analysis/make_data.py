{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pandas as pd\
import numpy as np\
\
# Column names based on your Healthcare project\
cols = ['visits', 'hospital', 'nursing', 'chronic', 'adls', 'age', 'income', \
        'gender', 'married', 'employed', 'insurance', 'medicaid', 'health', 'region']\
\
# Generate 100 rows of synthetic data\
np.random.seed(42)\
data = \{\
    'visits': np.random.poisson(5, 100),\
    'hospital': np.random.poisson(0.5, 100),\
    'nursing': np.random.poisson(0.1, 100),\
    'chronic': np.random.randint(0, 5, 100),\
    'adls': np.random.choice([0, 1], 100),\
    'age': np.round(np.random.uniform(6.5, 9.0, 100), 1),\
    'income': np.round(np.random.uniform(0.1, 5.0, 100), 4),\
    'gender': np.random.choice(['male', 'female'], 100),\
    'married': np.random.choice(['yes', 'no'], 100),\
    'employed': np.random.choice(['yes', 'no'], 100),\
    'insurance': np.random.choice(['yes', 'no'], 100),\
    'medicaid': np.random.choice(['yes', 'no'], 100),\
    'health': np.random.choice(['excellent', 'average', 'poor'], 100),\
    'region': np.random.choice(['northeast', 'midwest', 'south', 'west'], 100)\
\}\
\
df = pd.DataFrame(data)\
df.to_csv('NSMES1988.csv', index=False)\
print("File 'NSMES1988.csv' has been created in this folder!")}