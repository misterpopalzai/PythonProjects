import pandas as pd
from datetime import datetime, timedelta
import random
import xlsxwriter

# Simulate a mock database with sales data
def create_mock_database():
    products = ['Laptop', 'Phone', 'Tablet', 'Headphones']
    dates = [datetime(2025, 1, 1) + timedelta(days=x) for x in range(30)]
    data = {
        'Date': [],
        'Product': [],
        'Sales': [],
        'Revenue': []
    }
    
    for date in dates:
        for product in products:
            data['Date'].append(date)
            data['Product'].append(product)
            sales = random.randint(10, 100)
            data['Sales'].append(sales)
            data['Revenue'].append(sales * random.uniform(50, 500))
    
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%m/%d')
    return df

# Pull data from mock database
def pull_data():
    return create_mock_database()

# Export data to Excel with embedded chart using xlsxwriter
def export_to_excel_with_chart(df, filename='sales_data_with_chart.xlsx'):
    # Aggregate data by date
    agg_df = df.groupby('Date').agg({'Sales': 'sum', 'Revenue': 'sum'}).reset_index()
    
    # Create a new Excel workbook and add a worksheet
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet('Summary')
    data_worksheet = workbook.add_worksheet('Data')
    
    # Write headers for Data sheet
    data_worksheet.write_row(0, 0, df.columns)
    
    # Write data rows for Data sheet
    for row, data in enumerate(df.values, 1):
        data_worksheet.write_row(row, 0, data)
    
    # Write headers for Summary sheet
    worksheet.write_row(0, 0, agg_df.columns)
    
    # Write aggregated data rows for Summary sheet
    for row, data in enumerate(agg_df.values, 1):
        worksheet.write_row(row, 0, data)
    
    # Create a chart object
    chart = workbook.add_chart({'type': 'line'})
    
    # Configure the series for Revenue (red, primary axis)
    chart.add_series({
        'name': 'Sum of Revenue',
        'categories': '=Summary!$A$2:$A$31',
        'values': '=Summary!$C$2:$C$31',
        'line': {'color': 'red'},
        'marker': {'type': 'circle', 'size': 5, 'border': {'color': 'red'}, 'fill': {'color': 'red'}},
        'y2_axis': False,  # Primary axis
    })
    
    # Configure the series for Sales (blue, secondary axis)
    chart.add_series({
        'name': 'Sum of Sales',
        'categories': '=Summary!$A$2:$A$31',
        'values': '=Summary!$B$2:$B$31',
        'line': {'color': 'blue'},
        'marker': {'type': 'circle', 'size': 5, 'border': {'color': 'blue'}, 'fill': {'color': 'blue'}},
        'y2_axis': True,  # Secondary axis
    })
    
    # Add chart title and axis labels
    chart.set_title({'none': True})  # No title
    chart.set_x_axis({'name': 'Date', 'date_axis': True})
    chart.set_y_axis({'name': 'Values', 'major_gridlines': {'visible': True}})
    
    # Add a secondary y-axis
    chart.set_y2_axis({'name': 'Values', 'major_gridlines': {'visible': True}})
    
    # Insert the chart into the worksheet
    worksheet.insert_chart('D2', chart, {'x_scale': 1.5, 'y_scale': 1.5})
    
    # Close the workbook
    workbook.close()
    print(f"Data and chart exported to {filename}")

# Main execution
def main():
    df = pull_data()
    export_to_excel_with_chart(df)

if __name__ == "__main__":
    main()