import csv
import matplotlib.pyplot as plt
from colorama import Fore, Style

class Company:
    def __init__(self, name, business_type, forecasted_returns):
        self.name = name
        self.business_type = business_type
        self.forecasted_returns = forecasted_returns


class Investor:
    def __init__(self, email):
        self.email = email
        self.transactions = []

    def add_transaction(self, units, value, preference):
        transaction = {
            'units': units,
            'value': value,
            'preference': preference
        }
        self.transactions.append(transaction)


class Fund:
    def __init__(self, total_units):
        self.companies = []
        self.total_units = total_units
        self.units_issued = 0
        self.investors = []

    def add_company(self, company):
        self.companies.append(company)
        print(f"{Fore.GREEN}Added {company.name} to the fund.{Style.RESET_ALL}")

    def delete_company(self, company_name):
        for company in self.companies:
            if company.name == company_name:
                self.companies.remove(company)
                print(f"{Fore.RED}Deleted {company_name} from the fund.{Style.RESET_ALL}")
                return
        print(f"{company_name} not found in the fund.")

    def track_companies(self):
        print(f"\n{Fore.CYAN}Companies in the fund:{Style.RESET_ALL}")
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
            report = f"\n{Fore.YELLOW}--- Fund Report ---{Style.RESET_ALL}\n"
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
        plt.title(f"{Fore.MAGENTA}Fund Split by Business Type{Style.RESET_ALL}")
        plt.show()

    def save_as_csv(self):
        filename = "fund_data.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Business Type", "Forecasted Returns"])
            for company in self.companies:
                writer.writerow([company.name, company.business_type, company.forecasted_returns])
            
            writer.writerow([])  # Add an empty row
            
            writer.writerow(["Units Issued"])
            writer.writerow(["Total Units", self.total_units])
            writer.writerow(["Units Issued", self.units_issued])
            writer.writerow(["Units Remaining", self.total_units - self.units_issued])
            
            writer.writerow([])  # Add an empty row
            
            writer.writerow(["Investors"])
            writer.writerow(["Email"])
            for investor in self.investors:
                writer.writerow([investor.email])
            
            writer.writerow([])  # Add an empty row
            
            writer.writerow(["Investor Transactions"])
            writer.writerow(["Email", "Units", "Value", "Preference"])
            for investor in self.investors:
                for transaction in investor.transactions:
                    writer.writerow([investor.email, transaction['units'], transaction['value'], transaction['preference']])
        print(f"{Fore.GREEN}Fund data saved to {filename}.{Style.RESET_ALL}")

    def issue_units(self, units):
        if self.units_issued + units <= self.total_units:
            self.units_issued += units
            print(f"{Fore.GREEN}Issued {units} units.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Not enough units available to issue.{Style.RESET_ALL}")

    def add_investor(self, email):
        investor = Investor(email)
        self.investors.append(investor)
        print(f"{Fore.GREEN}Added investor with email {email}.{Style.RESET_ALL}")

    def add_investor_transaction(self, email, units, value, preference):
        for investor in self.investors:
            if investor.email == email:
                investor.add_transaction(units, value, preference)
                print(f"{Fore.GREEN}Added transaction for investor with email {email}.{Style.RESET_ALL}")
                return
        print(f"{Fore.RED}Investor with email {email} not found.{Style.RESET_ALL}")

    def track_investor_transactions(self, email):
        for investor in self.investors:
            if investor.email == email:
                print(f"\n{Fore.CYAN}Transactions for investor with email {email}:{Style.RESET_ALL}")
                if investor.transactions:
                    for transaction in investor.transactions:
                        print(f"Units: {transaction['units']}")
                        print(f"Value: {transaction['value']}")
                        print(f"Preference: {transaction['preference']}")
                        print()
                else:
                    print("No transactions found for the investor.")
                return
        print(f"{Fore.RED}Investor with email {email} not found.{Style.RESET_ALL}")

    def view_issued_units(self):
        print(f"\n{Fore.CYAN}Total Units Issued:{Style.RESET_ALL}")
        print(f"Units Issued: {self.units_issued}")
        print(f"Units Remaining: {self.total_units - self.units_issued}")
        print()

    def view_units_allocation(self):
        print(f"\n{Fore.CYAN}Units Allocation:{Style.RESET_ALL}")
        if self.investors:
            for investor in self.investors:
                total_units = 0
                for transaction in investor.transactions:
                    total_units += transaction['units']
                allocation_percentage = (total_units / self.units_issued) * 100
                print(f"Investor Email: {investor.email}")
                print(f"Allocated Units: {total_units}")
                print(f"Allocation Percentage: {allocation_percentage}%")
                print()
        else:
            print("No investors found.")
            print()


def add_company_to_fund(fund):
    print("\n" + "-" * 30)
    name = input("Enter the name of the company: ")
    business_type = input("Enter the type of business: ")
    forecasted_returns = input("Enter the forecasted returns (%): ")
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


def issue_units_to_fund(fund):
    print("\n" + "-" * 30)
    units = int(input("Enter the number of units to issue: "))
    fund.issue_units(units)


def add_investor(fund):
    print("\n" + "-" * 30)
    email = input("Enter the email of the investor: ")
    fund.add_investor(email)


def add_investor_transaction(fund):
    print("\n" + "-" * 30)
    email = input("Enter the email of the investor: ")
    units = int(input("Enter the number of units purchased: "))
    value = float(input("Enter the transaction value (NZD $): "))
    preference = input("Enter investment preference (specific businesses or whole fund): ")
    fund.add_investor_transaction(email, units, value, preference)


def track_investor_transactions(fund):
    print("\n" + "-" * 30)
    email = input("Enter the email of the investor: ")
    fund.track_investor_transactions(email)


def view_issued_units(fund):
    print("\n" + "-" * 30)
    fund.view_issued_units()


def view_units_allocation(fund):
    print("\n" + "-" * 30)
    fund.view_units_allocation()


def main():
    total_units = 1000  # Set the total units for the fund
    fund = Fund(total_units)

    while True:
        print("\n" + "=" * 30)
        print(f"{Fore.BLUE}--- Fund Management System ---{Style.RESET_ALL}")
        print("1. Add Company")
        print("2. Delete Company")
        print("3. Track Companies")
        print("4. Generate Fund Report")
        print("5. Generate Pie Chart")
        print("6. Save Fund Data as CSV")
        print("7. Issue Units")
        print("8. Add Investor")
        print("9. Add Investor Transaction")
        print("10. Track Investor Transactions")
        print("11. View Issued Units")
        print("12. View Units Allocation")
        print("13. Exit")

        choice = input("Enter your choice (1-13): ")

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
            issue_units_to_fund(fund)
        elif choice == "8":
            add_investor(fund)
        elif choice == "9":
            add_investor_transaction(fund)
        elif choice == "10":
            track_investor_transactions(fund)
        elif choice == "11":
            view_issued_units(fund)
        elif choice == "12":
            view_units_allocation(fund)
        elif choice == "13":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
