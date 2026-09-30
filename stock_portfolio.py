# ============================================================
#              📈 STOCK PORTFOLIO TRACKER PRO
# ============================================================
# Task 2 - Stock Portfolio Tracker
# Concepts: Dictionary, Input/Output, Arithmetic,
#           File Handling, Error Handling
# ============================================================


# ---------------- STOCK PRICE DATABASE ----------------

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "NVDA": 140,
    "AMZN": 195,
    "GOOGL": 165,
    "META": 560
}


# ---------------- DISPLAY STOCKS ----------------

def show_available_stocks():
    print("\n" + "=" * 55)
    print("              📊 AVAILABLE STOCKS")
    print("=" * 55)

    for stock, price in stock_prices.items():
        print(f"  {stock:<10} → ₹{price}")

    print("=" * 55)


# ---------------- GET STOCK DATA ----------------

def create_portfolio():
    portfolio = {}

    print("\n📌 Enter your stock details.")
    print("Type 'done' when you have finished.\n")

    while True:

        stock = input("Enter stock symbol: ").upper().strip()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("❌ Stock not found! Please choose from the available stocks.")
            continue

        # Quantity validation
        while True:
            try:
                quantity = int(input(f"Enter quantity of {stock}: "))

                if quantity <= 0:
                    print("❌ Quantity must be greater than 0.")
                    continue

                break

            except ValueError:
                print("❌ Please enter a valid whole number.")

        # If stock already exists, add quantity
        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity

        investment = stock_prices[stock] * quantity

        print(
            f"✅ Added {quantity} shares of {stock} "
            f"(Investment: ₹{investment:,})"
        )

    return portfolio


# ---------------- DISPLAY PORTFOLIO ----------------

def display_portfolio(portfolio):

    if not portfolio:
        print("\n❌ No stocks were added to the portfolio.")
        return 0

    print("\n")
    print("=" * 70)
    print("                    📈 YOUR PORTFOLIO")
    print("=" * 70)

    print(
        f"{'STOCK':<12}"
        f"{'PRICE':<15}"
        f"{'QUANTITY':<12}"
        f"{'INVESTMENT':<20}"
    )

    print("-" * 70)

    total_investment = 0
    highest_stock = ""
    highest_investment = 0

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        investment = price * quantity

        total_investment += investment

        if investment > highest_investment:
            highest_investment = investment
            highest_stock = stock

        print(
            f"{stock:<12}"
            f"₹{price:<14,}"
            f"{quantity:<12}"
            f"₹{investment:<19,}"
        )

    print("-" * 70)

    print(f"💰 TOTAL INVESTMENT : ₹{total_investment:,}")
    print(f"🏆 TOP INVESTMENT   : {highest_stock}")
    print(f"   Amount           : ₹{highest_investment:,}")

    print("=" * 70)

    return total_investment


# ---------------- SAVE TXT REPORT ----------------

def save_txt_report(portfolio, total):

    try:
        with open("portfolio_report.txt", "w", encoding="utf-8") as file:
            file.write("=" * 60 + "\n")
            file.write("           STOCK PORTFOLIO REPORT\n")
            file.write("=" * 60 + "\n\n")

            for stock, quantity in portfolio.items():

                price = stock_prices[stock]
                investment = price * quantity

                file.write(
                    f"{stock} | "
                    f"Price: ₹{price} | "
                    f"Quantity: {quantity} | "
                    f"Investment: ₹{investment}\n"
                )

            file.write("\n")
            file.write("-" * 60 + "\n")
            file.write(f"TOTAL INVESTMENT: ₹{total}\n")
            file.write("-" * 60 + "\n")

        print("\n📄 TXT report saved as: portfolio_report.txt")

    except Exception as error:
        print(f"❌ Error saving TXT file: {error}")


# ---------------- SAVE CSV REPORT ----------------

def save_csv_report(portfolio):

    try:
        with open("portfolio_data.csv", "w") as file:

            file.write("Stock,Price,Quantity,Investment\n")

            for stock, quantity in portfolio.items():

                price = stock_prices[stock]
                investment = price * quantity

                file.write(
                    f"{stock},{price},{quantity},{investment}\n"
                )

        print("📊 CSV report saved as: portfolio_data.csv")

    except Exception as error:
        print(f"❌ Error saving CSV file: {error}")


# ---------------- MAIN PROGRAM ----------------

def main():

    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + "       📈 STOCK PORTFOLIO TRACKER PRO".center(58) + "║")
    print("╠" + "═" * 58 + "╣")
    print("║" + " Track your investments using predefined stock prices ".center(58) + "║")
    print("╚" + "═" * 58 + "╝")

    show_available_stocks()

    portfolio = create_portfolio()

    if not portfolio:
        print("\n👋 No portfolio created. Goodbye!")
        return

    total = display_portfolio(portfolio)

    # Save reports
    print("\n💾 SAVING PORTFOLIO REPORT...")

    save_txt_report(portfolio, total)
    save_csv_report(portfolio)

    print("\n" + "=" * 60)
    print("       ✅ PORTFOLIO TRACKING COMPLETED!")
    print("=" * 60)
    print("📄 Your reports are ready.")
    print("🚀 Thank you for using Stock Portfolio Tracker Pro!")
    print("=" * 60)


# ---------------- RUN PROGRAM ----------------

if __name__ == "__main__":
    main()