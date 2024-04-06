import streamlit as st
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

st.title("Phone Number Location Finder")

# Get phone number from user input
number = st.text_input("Enter phone number (with country code):")

if number:
    pepnumber = phonenumbers.parse(number)
    location = geocoder.description_for_number(pepnumber, "en")
    service_pro = phonenumbers.parse(number)
    provider = carrier.name_for_number(service_pro, "en")

    st.write("Location:", location)
    st.write("Service Provider:", provider)

    key = '3229ea51ebed4311924d0dc704876aca'
    geocoder = OpenCageGeocode(key)
    query = str(location)
    results = geocoder.geocode(query)

    if results:
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']

        st.write("Latitude:", lat)
        st.write("Longitude:", lng)

        # Create a Basemap instance
        map = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,\
                llcrnrlon=-180,urcrnrlon=180,resolution='c')

        # Draw coastlines, countries, and states
        map.drawcoastlines()
        map.drawcountries()
        map.drawstates()

        # Convert latitude and longitude to Basemap coordinates
        x, y = map(lng, lat)

        # Plot a marker at the location
        map.plot(x, y, 'bo', markersize=8)

        # Show the plot
        plt.title("Location of Phone Number")
        st.pyplot(plt)
    else:
        st.error("No results found for the location.")