# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
from io import StringIO
import pandas as pd
from matplotlib import pyplot as plt
import csv
import numpy as np

LOGGER = get_logger(__name__)
def getGraph():
    try:
        X = []
        Y = []
        Y2 = []
        with open('growth.csv', 'r') as datafile:
            plotting = csv.reader(datafile, delimiter=';')

            for ROWS in plotting:
                X.append(float(ROWS[0]))
                Y.append(float(ROWS[1].replace(',','.')))
                Y2.append(float(ROWS[2].replace(',','.')))
        plt.bar(X,Y,align='edge',color='#0088cc')
        plt.bar(X,Y2,align='edge',color='#686e7a') 
        plt.xticks(np.arange(1,19,1))
        plt.title('График прироста цен по месяцам')
        plt.xlabel('Месяц')
        plt.ylabel('Цена')
        plt.savefig('growth.png')
    except Exception:
        return {"message":"error in generating plot"}
    
def getInfo():
    templates={"message":"generated succesfully"}
    return templates

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)

    getInfo()
    st.image("growth.png")
    


if __name__ == "__main__":
    run()
