import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile and Activities", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "Research Activities", "Contact"],
)

# Dummy STEM data
Thermoelectricity_data = pd.DataFrame({
    "Experiments": ["Thermoelectric Generator", "Thermoelectric Cooler", "Thermoelectric Heater"],
    "Average Resistance (ohm)": [4.9, 3.5, 3.4],
    "Mean Voltage (V)": [2.5, 8.0, 10.0],
    "Max Hotside Temp (°C)": [125.0, 20.0, 55.0],
    "Max Coldside Temp (°C)": [25.0, -10.0, 5.0],
    "Date": pd.date_range(start="2025-02-01", periods=3),
})

FuelCells_data = pd.DataFrame({
    "Fuel Cell Types": ["PEMFC", "SOFC", "AFC", "PAFC", "MCFC"],
    "Electrolyte Chemistry": ["Nafion", "YSZ", "KOH", "H3PO4", "Li-K CO3"],
    "Max Operating Temperatures (°C)": [100.0, 1000.0, 120.0, 200.0, 650.0],
    "Max Power Generation (MW)": [0.2, 1.5, 1.0, 2.0, 95.0],
    "Investigation Date": pd.date_range(start="2023-05-04", periods=5),
})

Nanosatellites_data = pd.DataFrame({
    "Form Factor (U)": [1, 3, 2],
    "Main Subsystems": ["PSU", "AD&C", "OBC&FS"],
    "CPUT's Main Missions": ["ZACUBE-1", "ZACUBE-2", "MDASat-1"],
    "Main Missions Altitude (km)": [600.0, 550, 525],
    "Main Missions Mass (kg)": [1.2, 4.0, 2.1],
    "Main Missions Year": [2013, 2018, 2022],
    "Researched Date": pd.date_range(start="2026-01-28", periods=3),
})

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Dr Nganyang Paul Bayendang"
    field = "Alternative Energy and Space & Satellite Systems Engineering"
    institution = "CPUT Smart Grid / UWC HySA Systems"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institutions:** {institution}")
    
    st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Nature (Pixabay)"
)

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "Research Activities":
    st.title("Research Activities")
    st.sidebar.header("Data Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Thermoelectricity Experiments", "Fuel Cells Research", "Nanosatellites"]
    )

    if data_option == "Thermoelectricity Experiments":
        st.write("### Thermoelectricity Experiment Data")
        st.dataframe(Thermoelectricity_data)
        # Add widget to filter by Resistance values
        resistance_filter = st.slider("Average Resistance (ohm)", 0.0, 5.0, (0.0, 5.0))
        voltage_filter = st.slider("Mean Voltage (V)", 0.0, 12.0, (0.0, 12.0))
        hstemp_filter = st.slider("Max Hotside Temp (°C)", 10.0, 150.0, (10.0, 150.0)) 
        cstemp_filter = st.slider("Max Coldside Temp (°C)", -10.0, 30.0, (-10.0, 30.0)) 
        filtered_thermoelectricity = Thermoelectricity_data[
            Thermoelectricity_data["Average Resistance (ohm)"].between(resistance_filter[0], resistance_filter[1]) &
            Thermoelectricity_data["Mean Voltage (V)"].between(voltage_filter[0], voltage_filter[1]) &
            Thermoelectricity_data["Max Hotside Temp (°C)"].between(hstemp_filter[0], hstemp_filter[1]) &
            Thermoelectricity_data["Max Coldside Temp (°C)"].between(cstemp_filter[0], cstemp_filter[1])
        ]
        st.write(f"Filtered Results for Resistance Range {resistance_filter}, Voltage {voltage_filter}, Max Hotside Temp {hstemp_filter} and Max Coldside Temp {cstemp_filter}:")
        st.dataframe(filtered_thermoelectricity)

    elif data_option == "Fuel Cells Research":
        st.write("### Fuel Cells Research Data")
        st.dataframe(FuelCells_data)
        # Add widget to filter by Electrolyte, Temperature and Power
        temperature_filter = st.slider("Filter by Max Operating Temperatures (°C)", 50.0, 1000.0, (50.0, 1000.0))
        power_filter = st.slider("Filter by Max Power Generation (MW)", 0.1, 100.0, (0.1, 100.0))

        filtered_fuelcells = FuelCells_data[
            FuelCells_data["Max Operating Temperatures (°C)"].between(temperature_filter[0], temperature_filter[1]) &
            FuelCells_data["Max Power Generation (MW)"].between(power_filter[0], power_filter[1])
        ]
        st.write(f"Filtered Results for Max Operating Temperatures {temperature_filter} and Power Generation {power_filter}:")
        st.dataframe(filtered_fuelcells)

    elif data_option == "Nanosatellites":
        st.write("### Nanosatellites Design Details")
        st.dataframe(Nanosatellites_data)
        # Add widgets to filter by form factor and mass
        formfactor_filter = st.slider("Filter by Form Factor (U)", 1, 3, (1, 3))
        mass_filter = st.slider("Filter by Main Missions Mass (kg)", 1.0, 5.0, (1.0, 5.0))
        altitude_filter = st.slider("Filter by Main Missions Altitude (km)", 400.0, 600.0, (400.0, 600.0))
        year_filter = st.slider("Filter by Main Missions Year", 2012, 2022, (2012, 2022))
        filtered_nanosats = Nanosatellites_data[
            Nanosatellites_data["Form Factor (U)"].between(formfactor_filter[0], formfactor_filter[1]) &
            Nanosatellites_data["Main Missions Mass (kg)"].between(mass_filter[0], mass_filter[1]) &
            Nanosatellites_data["Main Missions Altitude (km)"].between(altitude_filter[0], altitude_filter[1]) &
            Nanosatellites_data["Main Missions Year"].between(year_filter[0], year_filter[1])
        ]
        st.write(f"Filtered Results for Form Factor {formfactor_filter}, Main Missions Mass {mass_filter}, Main Missions Altitude {altitude_filter} and Main Missions Year {year_filter}:")
        st.dataframe(filtered_nanosats)
        
        

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "bayendang@live.co.za"
    phone = "0123456789"
    st.write(f"You can email me to: {email}")
    st.write(f"You can phone me on: {phone}")

    