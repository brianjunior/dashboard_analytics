import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
from streamlit_option_menu import option_menu

# Import matplotlib for background_gradient
try:
    import matplotlib.pyplot as plt
    from matplotlib.colors import LinearSegmentedColormap
    matplotlib_available = True
except ImportError:
    matplotlib_available = False
    st.warning("matplotlib is not installed. Gradient background will not be displayed.")

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Portfolio & Latefile Analysis!!!", page_icon=":bar_chart", layout="wide")

st.title(":bar_chart: PORTFOLIOS & LATEFILE ANALYSIS")
st.markdown('<style>div.block-container{padding-top:2.3rem;}', unsafe_allow_html=True)

# Function to read the CSV files
def load_data(file1, file2):
    data1, data2 = None, None
    
    # Check if both files exist
    if os.path.exists(file1) and os.path.exists(file2):
        try:
            # Read both CSV files
            data1 = pd.read_csv(file1)
            data2 = pd.read_csv(file2)
            st.success("Your Feedback & Reactions Matter!")
        except Exception as e:
            st.error(f"An error occurred while loading the files: {e}")
    else:
        st.error("One or both files not found. Please check the file paths.")
    
    return data1, data2

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('MICROFIN UGANDA LIMITED',
                           [
                            '2024',
                            '2025',
                           ],
                           menu_icon='hospital-fill',
                           icons=['activity', 'activity'],
                           default_index=0)

# Load both data files
file_path1 = 'file.csv'  # Path to the first file
file_path2 = 'late.csv'  # Path to the second file

data1, data2 = load_data(file_path1, file_path2)

# if selected == 'Overview' and data1 is not None and data2 is not None:
#     # Clean the data: Convert columns to numeric, replace commas, and coerce errors
#     data1.iloc[:, 1:] = data1.iloc[:, 1:].replace({',': ''}, regex=True).apply(pd.to_numeric, errors='coerce')
#     data2.iloc[:, 1:] = data2.iloc[:, 1:].replace({',': ''}, regex=True).apply(pd.to_numeric, errors='coerce')
    
#     # Overall total loan disbursements sum from file.csv
#     total_disbursements = data1.iloc[:, 1:].sum().sum()  # Sum of all columns except 'BRANCH'

#     # Overall total sum from late.csv (the 'TOTAL' column)
#     total_late = data2['TOTAL'].sum()

#     # Calculate total disbursements per branch from file.csv
#     data1['Total Disbursements'] = data1.iloc[:, 1:].sum(axis=1)

#     # Add new row for total disbursements summary
#     total_row = pd.DataFrame(data1[['BRANCH', 'Total Disbursements']].sum(axis=0)).T
#     total_row['BRANCH'] = 'Total Disbursements'
#     data1 = pd.concat([data1, total_row], ignore_index=True)

#     # Calculate the late file amount per branch from late.csv
#     data2['Late File Amount'] = data2['TOTAL']

#     # Add new row for total late file summary
#     total_late_row = pd.DataFrame(data2[['BRANCH', 'Late File Amount']].sum(axis=0)).T
#     total_late_row['BRANCH'] = 'Total Late File'
#     data2 = pd.concat([data2, total_late_row], ignore_index=True)

#     # Remove the "Total" row from the data for the disbursement line plot and late file plot
#     data1_without_total = data1[data1['BRANCH'] != 'Total Disbursements']
#     data2_without_total = data2[data2['BRANCH'] != 'Total Late File']

#     # Create the overall total disbursements chart
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown(f"<h5 style='text-align: center; font-size: 14px;'>Overall Total Portfolios</h5>", unsafe_allow_html=True)
#         st.markdown(f"<h3 style='text-align: center; font-weight: bold;'>UGX {total_disbursements:,.2f}</h2>", unsafe_allow_html=True)
    
#     with col2:
#         st.markdown(f"<h5 style='text-align: center; font-size: 14px;'>Overall Total Late File Amount</h5>", unsafe_allow_html=True)
#         st.markdown(f"<h3 style='text-align: center; font-weight: bold;'>UGX {total_late:,.2f}</h2>", unsafe_allow_html=True)

#     # Create the line graph for total disbursements per branch
#     fig_disbursements = px.line(data1_without_total, x='BRANCH', y='Total Disbursements', 
#                                 title="Overall Portfolios per Branch", 
#                                 labels={'Total Disbursements': 'UGX Total Disbursements'},
#                                 markers=True)
    
#     # Display the total disbursements chart
#     st.plotly_chart(fig_disbursements)

#     # Create the line graph for total late file amount per branch (red color)
#     fig_late = px.line(data2_without_total, x='BRANCH', y='Late File Amount', 
#                        title="Overall Late File per Branch", 
#                        labels={'Late File Amount': 'UGX Late File Amount'},
#                        markers=True)

#     # Change the color of the line to red
#     fig_late.update_traces(line=dict(color='red'))

#     # Display the late file chart
#     st.plotly_chart(fig_late)

#     # STEP 1: Aggregate the data by month for `file.csv` (Total Disbursements)
#     data1_monthly = data1.drop(columns=['BRANCH'])
#     data1_monthly = data1_monthly.sum(axis=0).reset_index()
#     data1_monthly.columns = ['Month', 'Total Disbursements']

#     # STEP 2: Aggregate the data by month for `late.csv` (Late File Amount)
#     data2_monthly = data2.drop(columns=['BRANCH'])
#     data2_monthly = data2_monthly.sum(axis=0).reset_index()
#     data2_monthly.columns = ['Month', 'Late File Amount']

#     # STEP 3: Remove the "Total" row from monthly data for both
#     data1_monthly_without_total = data1_monthly[data1_monthly['Month'] != 'TOTAL']
#     data2_monthly_without_total = data2_monthly[data2_monthly['Month'] != 'TOTAL']

#     # Remove the "TOTAL" month column if it exists at the extreme end of both datasets
#     data1_monthly_without_total = data1_monthly_without_total[data1_monthly_without_total['Month'] != 'TOTAL']
#     data2_monthly_without_total = data2_monthly_without_total[data2_monthly_without_total['Month'] != 'TOTAL']

#     # STEP 4: Plot the line graph for the total disbursements per month (green line)
#     fig_total_monthly = px.line(data1_monthly_without_total, x='Month', y='Total Disbursements', 
#                                 title="Total Portfolios per Month", 
#                                 labels={'Total Disbursements': 'UGX Total Disbursements'},
#                                 markers=True)

#     # Set the line color to green
#     fig_total_monthly.update_traces(line=dict(color='green'))

#     # STEP 5: Plot the line graph for the total late file amount per month (red line)
#     fig_late_monthly = px.line(data2_monthly_without_total, x='Month', y='Late File Amount', 
#                                title="Late File Amount per Month", 
#                                labels={'Late File Amount': 'UGX Late File Amount'},
#                                markers=True)

#     # Set the line color to red
#     fig_late_monthly.update_traces(line=dict(color='red'))

#     # STEP 6: Display both charts
#     st.plotly_chart(fig_total_monthly)
#     st.plotly_chart(fig_late_monthly)


if selected == '2024' and data1 is not None and data2 is not None:
    # Clean the data: Convert columns to numeric, replace commas, and coerce errors
    data1.iloc[:, 1:] = data1.iloc[:, 1:].replace({',': ''}, regex=True).apply(pd.to_numeric, errors='coerce')
    data2.iloc[:, 1:] = data2.iloc[:, 1:].replace({',': ''}, regex=True).apply(pd.to_numeric, errors='coerce')

    # List of branches you specified
    branches = ['IGANGA', 'GULU', 'MAYUGE', 'PALLISA', 'KAMULI', 'HOIMA', 'KUMI', 
                'ARUA', 'KOBOKO', 'JINJA', 'ADJUMANI', 'MASAKA', 'NEBBI', 'KITGUM', 
                'NANSANA', 'KAGADI', 'FORT PORTAL']

    # Loop through each branch to create the graphs for disbursements and late file amounts
    for branch in branches:
        st.subheader(f"Branch: {branch}")

        # Filter data for the branch in both datasets
        branch_data1 = data1[data1['BRANCH'] == branch].drop(columns=['BRANCH'])
        branch_data2 = data2[data2['BRANCH'] == branch].drop(columns=['BRANCH'])

        # Step 1: Create the line graph for monthly disbursements for this branch
        branch_data1_monthly = branch_data1.transpose().reset_index()
        branch_data1_monthly.columns = ['Month', 'Disbursements']
        
        # Remove the "TOTAL" if it appears in the columns
        branch_data1_monthly = branch_data1_monthly[branch_data1_monthly['Month'] != 'TOTAL']
        
        # Plot the line graph for disbursements
        fig_disbursements = px.line(branch_data1_monthly, x='Month', y='Disbursements', 
                                    title=f"Monthly Portfolio Trend for {branch} (2024)", 
                                    labels={'Disbursements': 'UGX Portfolios'}, markers=True)
        fig_disbursements.update_traces(line=dict(color='green'))  # Set line color to green
        
        # Display the monthly disbursements graph
        st.plotly_chart(fig_disbursements)

        # Step 2: Create the line graph for monthly late file amounts for this branch
        branch_data2_monthly = branch_data2.transpose().reset_index()

        # Debug: Check the shape of branch_data2_monthly to understand what columns are present
        # st.write("Shape of branch_data2_monthly:", branch_data2_monthly.shape)
        # st.write("Columns of branch_data2_monthly:", branch_data2_monthly.columns)

        # Ensure proper column names (Month and Late File Amount)
        # Check if the transposition results in two columns, if not, handle accordingly
        if branch_data2_monthly.shape[1] > 1:
            branch_data2_monthly.columns = ['Month', 'Late File Amount']
        else:
            # If there is an unexpected shape (like a single column), handle accordingly
            st.write("Unexpected shape, adjusting column names manually.")
            branch_data2_monthly.columns = ['Month'] + branch_data2_monthly.columns.tolist()[1:]

        # Remove the "TOTAL" if it appears in the columns
        branch_data2_monthly = branch_data2_monthly[branch_data2_monthly['Month'] != 'TOTAL']

        # Plot the line graph for late file amounts
        fig_late = px.line(branch_data2_monthly, x='Month', y='Late File Amount', 
                           title=f"Monthly Late File Trend for {branch} (2024)", 
                           labels={'Late File Amount': 'UGX Late File Amount'}, markers=True)
        fig_late.update_traces(line=dict(color='red'))  # Set line color to red

        # Display the monthly late file graph
        st.plotly_chart(fig_late)
