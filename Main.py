from pathlib import Path

# Creates summary_report.txt file 
fp_summarytext = Path.cwd()/"summary_report.txt"
fp_summarytext.touch()

# Imports data from the other files in project_group
import api, cash_on_hand, overheads, profit_loss

def main():
    """
    - This function returns a list several values 
        - REAL TIME CURRENCY CONVERSION RATE
        - HIGHEST OVERHEADS
        - CASH DEFICIT or CASH SURPLUS
        - PROFIT DEFICIT or PROFIT SURPLUS
    - No parameters required
    """
    try:
        coh_value2 = []
        pnl_value2 = []

        # Assigns data from the imported files variables
        forex = api.api_exchange()
        # Forex placed into parameter for functions from imported files
        # Converted data assigned to different variables
        overhead_value = overheads.overhead(forex)
        coh_value = cash_on_hand.cashdata(forex)
        pnl_value = profit_loss.profit_loss_data(forex)

        # Checks if imported profit_loss data equates to a statement
        if pnl_value == "NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY":
            # If true, the statement is appended into pnl_value2
            pnl_value2.append(f"\n[PROFIT SURPLUS] {pnl_value}")

        else:
            # If false, data is appended into pnl_value2 as a statement
            for i in range(len(pnl_value)):
                pnl_value2.append(f"\n[PROFIT DEFICIT] DAY: {pnl_value[i][0]} AMOUNT: SGD{pnl_value[i][1]}")

        # Checks if imported cash_on_hand data equates to a statement
        if coh_value == "CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY":
            # If true, the statement is appended into coh_value2
            coh_value2.append(f"\n[CASH SURPLUS] {coh_value}")
        else:
            # If false, data is appended into coh_value2 as a statement
            for k in range(len(coh_value)):
                coh_value2.append(f"\n[CASH DEFICIT] DAY: {coh_value[k][0]} AMOUNT: SGD{coh_value[k][1]}")

        # Data from api is converted into a statement and assigned as first        
        first = f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}"
        # Data from overheads is converted into a statement and assigned as second
        second = f"\n[HIGHEST OVERHEADS] {overhead_value[0]}: SGD{overhead_value[1]}"
        # Variables first and second placed into a list
        list = [first, second]
        # Data in coh_value2 and pnl_value2 placed into the list
        list.extend(coh_value2)
        list.extend(pnl_value2)
        # Returns list
        return list
    # except stops the code from crashing and provides a message for the error
    except Exception as e:
        return f"AN ERROR HAS OCCURED. \nREASON: {e}"

# Writes data from list into summary_report.txt file
with fp_summarytext.open(mode="w", encoding="UTF-8", newline="") as file:
    file.writelines(main())