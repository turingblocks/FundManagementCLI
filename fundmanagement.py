import csv
import matplotlib.pyplot as plt

class Company:
    def __init__(self, name, business_type, forecasted_returns):
        self.name = name
        self.business_type = business_type
        self.forecasted_returns = forecasted_returns


class Fund:
    def __init__(self):
        self.companies = []

    def add_company(self, company):
        self.companies.append(company)
        print(f"Added {company.name} to the fund.")

    def delete_company(self, company_name):
        for company in self.companies:
            if company.name == company_name:
                self.companies.remove(company)
                print(f"Deleted {company_name} from the fund.")
                return
        print(f"{company_name} not found in the fund.")

    def track_companies(self):
        print("Companies in the fund:")
        if self.companies:
            for company in self.companies:
                print(f"Name: {company.name}")
                print(f"Business Type: {company.business_type}")
                print(f"Forecasted Returns: {company.forecasted_returns}")
                print()
        else:
            print("No companies in the fund.")

    def generate_report(self):
        if self.companies:
            report = "--- Fund Report ---\n"
            for company in self.companies:
                report += f"Name: {company.name}\n"
                report += f"Business Type: {company.business_type}\n"
                report += f"Forecasted Returns: {company.forecasted_returns}\n\n"
            return report
        else:
            return "No companies in the fund."

    def generate_pie_chart(self):
        business_types = {}
        for company in self.companies:
            if company.business_type in business_types:
                business_types[company.business_type] += 1
            else:
                business_types[company.business_type] = 1

        labels = list(business_types.keys())
        sizes = list(business_types.values())

        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.title('Fund Split by Business Type')
        plt.show()

    def save_as_csv(self):
        filename = "fund_data.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Business Type", "Forecasted Returns"])
            for company in self.companies:
                writer.writerow([company.name, company.business_type, company.forecasted_returns])
        print(f"Fund data saved to {filename}.")


def add_company_to_fund(fund):
    print("\n" + "-" * 30)
    name = input("Enter the name of the company: ")
    business_type = input("Enter the type of business: ")
    forecasted_returns = float(input("Enter the forecasted returns: "))
    company = Company(name, business_type, forecasted_returns)
    fund.add_company(company)


def delete_company_from_fund(fund):
    print("\n" + "-" * 30)
    company_name = input("Enter the name of the company to delete: ")
    fund.delete_company(company_name)


def track_companies_in_fund(fund):
    print("\n" + "-" * 30)
    fund.track_companies()


def generate_fund_report(fund):
    print("\n" + "-" * 30)
    report = fund.generate_report()
    print(report)


def generate_pie_chart(fund):
    print("\n" + "-" * 30)
    fund.generate_pie_chart()


def save_fund_data(fund):
    print("\n" + "-" * 30)
    fund.save_as_csv()


def main():
    fund = Fund()

    while True:
        print("\n" + "=" * 30)
        print("--- Fund Management System ---")
        print("1. Add Company")
        print("2. Delete Company")
        print("3. Track Companies")
        print("4. Generate Fund Report")
        print("5. Generate Pie Chart")
        print("6. Save Fund Data as CSV")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_company_to_fund(fund)
        elif choice == "2":
            delete_company_from_fund(fund)
        elif choice == "3":
            track_companies_in_fund(fund)
        elif choice == "4":
            generate_fund_report(fund)
        elif choice == "5":
            generate_pie_chart(fund)
        elif choice == "6":
            save_fund_data(fund)
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
