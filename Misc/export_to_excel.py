import pyodbc
import xlsxwriter

# Database connection (update SERVER with your instance)
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=BU-XPS\SQLEXPRESS;DATABASE=JobDemoDB;Trusted_Connection=yes')
cursor = conn.cursor()

# Query Temperature Data
cursor.execute("SELECT Date, High_F, Low_F FROM TemperatureData")
temperature_data = cursor.fetchall()

# Query Salary Data
cursor.execute("SELECT Name, Company, Salary FROM SalaryData")
salary_data = cursor.fetchall()

# Create Excel file
workbook = xlsxwriter.Workbook('JobDemoOutput.xlsx')
worksheet = workbook.add_worksheet('Temperature')
worksheet2 = workbook.add_worksheet('Salary')

# Write Temperature Data
worksheet.write('A1', 'Date')
worksheet.write('B1', 'High (°F)')
worksheet.write('C1', 'Low (°F)')
for row, data in enumerate(temperature_data):
    worksheet.write(row + 1, 0, str(data[0]))
    worksheet.write(row + 1, 1, data[1])
    worksheet.write(row + 1, 2, data[2])

# Write Salary Data
worksheet2.write('A1', 'Name')
worksheet2.write('B1', 'Company')
worksheet2.write('C1', 'Salary')
for row, data in enumerate(salary_data):
    worksheet2.write(row + 1, 0, data[0])
    worksheet2.write(row + 1, 1, data[1])
    worksheet2.write(row + 1, 2, data[2])

workbook.close()
conn.close()