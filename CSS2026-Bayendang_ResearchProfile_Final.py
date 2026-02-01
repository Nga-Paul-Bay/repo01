
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from datetime import datetime



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
    field = "Alternative Energy, Space & Satellite Systems Engineering and Model-based Designs / Mathematical Modelling"
    institution = "CPUT's Energy Institute / F'SATI and UWC's HySA Systems"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Current Research Interests:** {field}")
    st.write(f"**Institutions:** {institution}")
    
    
    # Tabbed view for STEM data
    profile_option = st.sidebar.selectbox(
        "Select research sample option:",
        ["Research Pictures Sample", "Research Videos Sample"]
    )
    
      
    
    if profile_option == "Research Pictures Sample":
            st.write("### Selected Research Pictures Displayed")
           
            # Ensure you have local image files named image1.jpg, image2.jpg, and image3.jpg
            image_paths = ["https://media.licdn.com/dms/image/v2/D4E22AQFJbi9UXWCDvw/feedshare-shrink_800/B4EZifVO_vHIAs-/0/1755019810201?e=2147483647&v=beta&t=O5kV-SM9ZLQassGeJWiJdihp9Fo-zPJ3g5xVfu-2YAk","https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/ce/7/2/10.1093_ce_zkac079/3/m_zkac079_fig59.jpeg?Expires=1772176898&Signature=QtNupSBV6OqkaglbvughvxQ2CmEPGr9qg8K4rmCl7a~0JGTGwvxF6u6dkcKfrY1m2FoU5xlySGQlDdDpA9Y7wBgCC28gF7QfzvCbVcZwckHg34b02Jbo001KT2BaaOckORro26ru9Gw4xE2TrBoRRJHqT7GmUpQDFrxrr2OCtXqWNNTNblE3hmheH1ePRPOgyqRDOUedLq5RcA6sdPH1Dyv08KlpWkVIXtQtxxTI6nSaAeT8QBvJv7OqeybG1yUFmh91qiz3QzORM6N45~g8nuzkQqgQgi6~IgtJMGJw0SVIiA6QISsQGqByyBWJS01VvIuZxiP1UuDtc~prSf3bOA__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA"]
            captions = ["CPUT F'SATI CubeSat ZACUBE-1 Backdrop", "Combined Cold, Heat & Power (CCHP) System"]
        
            st.image(image_paths, caption=captions, width=550)        
                                
            
            #Ensure you have local image files named image1.jpg, image2.jpg, and image3.jpg
            image_paths = ["https://onlinelibrary.wiley.com/cms/asset/89fbda9c-3075-41f1-91b3-2265dce922cc/eng213061-fig-0005-m.jpg", "https://www.researchgate.net/publication/349058947/figure/fig1/AS:1004886460203009@1616595010541/TEC-original-model-based-on-MatLab-Simulink.png"]
            captions = ["Thermoelectricity Experiments Test Setup", "GUI of nxn Thermoelectric Cooler Modelling with MATLAB/Simulink"]
        
            st.image(image_paths, caption=captions, width=550)
    
    
            #Ensure you have local image files named image1.jpg, image2.jpg, and image3.jpg
            image_paths = ["https://astesj.com/wp-content/uploads/2022/03/1b-2.png","https://www.researchgate.net/publication/358580397/figure/fig2/AS:1123308305166338@1644828978916/d-TEGs-modeling-and-simulation-TEGs-engine.jpg"]
            captions = ["GUI of nxn Thermoelectric Generator Modelling with MATLAB/Simulink","Interior of Thermoelectric Generator Modelling with MATLAB/Simulink"]
        
            st.image(image_paths, caption=captions, width=550)
    
    elif profile_option == "Research Videos Sample":
            st.write("### Research Sample Videos Selected (Courtesy of SSTL): Click Play to Watch")
       
    
    #st.video("https://www.youtube.com/watch?v=xoJsk92cwtw", start_time=10)
    # st.image("https://drive.google.com/file/d/1EU74vSpSxZ84SQlEFWh9q0jRpr63J1ND/view?usp=drive_linkg",
    # caption="Nature (Pixabay)")
    
    
            DEFAULT_WIDTH = 75
            VIDEO_DATA = "https://www.youtube.com/watch?v=xoJsk92cwtw"
            
            st.set_page_config(layout="wide")
            
            width = st.sidebar.slider(
                label="Slide to adjust video size", min_value=25, max_value=100, value=DEFAULT_WIDTH, format="%d%%"
            )
            
            width = max(width, 0.01)
            side = max((100 - width) / 2, 0.01)
            
            _, container, _ = st.columns([side, width, side])
            container.video(data=VIDEO_DATA)
    
    

elif menu == "Publications":
    st.title("My DHET Accredited Publications")
    st.sidebar.header("Publications Selection:")

    
    # Tabbed view for STEM data
    publication_option = st.sidebar.selectbox(
        "Please choose upload option:",
        ["Auto-load publications from Google Drive", "Manually upload publications from CSV file"]
    )
    
    
    def publishedpapers (articles):
                                     
                # Add filtering for year or keyword
                keyword = st.text_input("Filter by keyword (NB: enter in full either the author name, article title, publication (journal name) or publisher)", "") 
               
                if keyword:
                    filtered = publications[
                        publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
                    ]
                    st.write(f"Filtered Results for '{keyword}':")
                    st.dataframe(filtered)
           
                else:
                    # publication_count = st.dataframe(publications)
                    publications_total = len(publications)

                    # Display the row counts
                    # st.write("### Total Publications Count")
                    st.write(f"Showing all publications: **{publications_total}** in total.")
                    
                # Publication trends
                if "Year" in publications.columns:
                    st.subheader("Publication Trends")
                    year_counts = publications["Year"].value_counts().sort_index()
                    st.bar_chart(year_counts)
                else:
                    st.write("The CSV does not have a 'Year' column to visualize trends.")
                    
   
    
    if publication_option == "Auto-load publications from Google Drive":
            st.write("### Publications in Google Drive Automatically Loaded")
           
            url='https://drive.google.com/file/d/1hqpkwf4wqjdJCbL6JlQ9iFuxadUPaV2A/view?usp=drive_link'
            url='https://drive.google.com/uc?id=' + url.split('/')[-2]

            publications = pd.read_csv(url)
            
            st.dataframe(publications) 
            
            publishedpapers (publications)

                
    
    elif publication_option == "Manually upload publications from CSV file":
                st.write("### Publications will be manually uploaded")
                st.sidebar.header("Upload and Filter")

                # Upload publications file
                uploaded_file =""
                uploaded_file = st.file_uploader("Upload a CSV file with publications.", type="csv")
                  
                
                if uploaded_file is not None:
                            publications = pd.read_csv(uploaded_file)
                            st.dataframe(publications)
                            
                            publishedpapers (publications)
            
                else:
                            st.write("Please upload a CSV file with publications to proceed.")


elif menu == "Research Activities":
    st.title("Research Activities")
    st.sidebar.header("Research Data Selection:")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Please choose a dataset to view:", 
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
    st.write("**For more info, you may use the below resources to connect / to know more / engage further.**")
    captions = ["Email: mysurname@live.co.za","Phone / Text:         0123456789"]
    image_paths = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhIFqTqakCu_CRznkL8agN8l-c178R81guaA&s","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjroqW8raszSzsOHlRao4541E_-oL59g5EqA&s"]
    st.image(image_paths, caption=captions, width=150)   
    
    captions = ["LinkedIn: https://www.linkedin.com/in/nganyang-paul-bayendang-435a8330/"]
    image_paths = ["https://cdn.produkto.io/photos/2025/04/22/linkedin-logo-2019.webp"]
    st.image(image_paths, caption=captions, width=400) 
    
    captions = ["Research: https://www.researchgate.net/profile/Nganyang-Bayendang/research"]
    image_paths = ["https://i.sstatic.net/TxT1R.png"]
    st.image(image_paths, caption=captions, width=150) 
    
    captions = ["GoogleScholar: https://scholar.google.com/citations?user=8p8YmSIAAAAJ&hl=en"]
    image_paths = ["https://logowik.com/content/uploads/images/google-scholar4372.jpg"]
    st.image(image_paths, caption=captions, width=250) 
    
    
    # email = "mysurname@live.co.za"
    # phone = "0123456789"
    # LinkedIn = "https://www.linkedin.com/in/nganyang-paul-bayendang-435a8330/"
    # ResearchGate = "https://www.researchgate.net/profile/Nganyang-Bayendang/research"
    # GoogleScholar = "https://scholar.google.com/citations?user=8p8YmSIAAAAJ&hl=en"
    
    # st.write(f"You can email me to: {email}")
    # st.write(f"You may phone me on: {phone}")
    # st.write(f"We can also link up on: {LinkedIn}")
    # st.write(f"We may also connect on: {ResearchGate}")
    # st.write(f"You may also check some of my published research on: {GoogleScholar}")

    # Get the current date and time
    current_datetime = datetime.now()
    
    # Print the result
    st.write(" ")
    st.write("**Created on January 31, 2026**")
    st.write(f"### Current Date and Time: {current_datetime}")


    
