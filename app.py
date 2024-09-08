import pandas as pd 
import streamlit as st
# Sugar Bag Dataset


st.set_page_config( 
    page_title="Ubarn Smart AI", 
    page_icon=":bar_chart:", 
    layout="wide")

file_paths_sugar_bag = {
    'weather_station': './SugarBag/SugarBagRd_Atmos_Aggregated.csv',
    'wifi_counter': './SugarBag/SugarBagRd_NCount_Aggregated.csv',
    'object_detection': './SugarBag/Alpha_X_Aggregated.csv',
    'infrared_bi_directional': './SugarBag/SugarBagRd_Farmo_Aggregated.csv',
    'infrared_counters': './SugarBag/SugarBagRd_DingTek_Aggregated.csv',
    'vibration_counters': './SugarBag/SugarBagRd_R718mbb_Aggregated.csv'

}


# Mary Cairncross

file_path_mary_cairncross = {
    'weather_station': './MaryCaincross/Atmos_Aggregated.csv',
    'wifi_counter': './MaryCaincross/NCount_Aggregated.csv',
    'object_detection': './MaryCaincross/Milesight_Aggregated.csv',
    'infrared_bi_directional': './MaryCaincross/Farmo_Aggregated.csv',
    'infrared_counters': './MaryCaincross/DingTek_Aggregated.csv',
    'soil_moisture_sensor': './MaryCaincross/SMT100a_Aggregated.csv',
    'environment_monitoring': './MaryCaincross/R712_Aggregated.csv',
    'temperature_probes': './MaryCaincross/R718b140_Aggregated.csv'

}

# Funtioin to load datasets

def load_dataset(file_path):
    return pd.read_csv(file_path)

# Sugar datasets

sugar_bag_data = { sensor: load_dataset(path) for sensor, path in file_paths_sugar_bag.items()}

# Mary Cairncross 

mary_cairncross_data= { sensor: load_dataset(path) for sensor, path in file_path_mary_cairncross.items()}

# Cleaning dataset


# Weather Station 
def clean_weather_data(df):
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['Month'] = pd.to_datetime(df['datetime'], format='%m').dt.month_name()
    df['Year'] = pd.DatetimeIndex(df['datetime']).year
    return df

sugar_bag_data['weather_station']= clean_weather_data(sugar_bag_data['weather_station'])

st.dataframe(sugar_bag_data['weather_station'])






