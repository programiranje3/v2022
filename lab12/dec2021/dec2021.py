import csv
from pathlib import Path
from sys import stderr
from pprint import pprint
from collections import defaultdict
from datetime import datetime as dt


def read_from_csv(fpath):
    data = []
    try:
        with open(fpath, 'r') as fobj:
             for row_data in csv.DictReader(fobj):
                 data.append(row_data)
    except FileNotFoundError:
        stderr.write(f"File {fpath} could not be found -> cannot proceed!\n")
    except OSError as err:
        stderr.write(f"An error occurred while trying to read data from the csv file:{fpath}\n{err}\n")
    finally:
        return data


def read_data_from_csv_v2(fpath):
    data = []
    row_cnt = 0
    column_names = []
    try:
        with open(fpath, "r") as fobj:
            for csv_row in csv.reader(fobj):
                if row_cnt == 0:
                    column_names = csv_row
                else:
                    d = dict()
                    for label, value in zip(column_names, csv_row):
                        d[label] = value
                    data.append(d)
                row_cnt += 1
    except FileNotFoundError:
        stderr.write(f"File {fpath} could not be found -> cannot proceed!\n")
    except OSError as e:
        stderr.write(f"An error occurred while trying to read data from the csv file:{fpath}\n{e}\n")
    finally:
        return data


def highest_round_a_investments(investments_data):
    round_a_dict = defaultdict(list)
    for investment in investments_data:
        if investment['round'] != 'a':
            continue
        try:
            funded_dt = dt.strptime(investment['fundedDate'], '%d-%b-%y')
        except ValueError as err:
            stderr.write(f"Error occurred when trying to parse {investment['fundedDate']} to date:\n{err}\n")
        else:
            if 2005 <= funded_dt.year <= 2008:
                company_funds = investment['company'], float(investment['raisedAmt'])
                round_a_dict[funded_dt.year].append(company_funds)

    results_dict = dict()
    for inv_year, investments in round_a_dict.items():
        results_dict[inv_year] = max(investments, key=lambda inv: inv[1])

    return results_dict


def year_state_stats(investments_data):

    year_state_amount = defaultdict(float)
    year_state_cities = defaultdict(set)
    for investment in investments_data:
        try:
            investment['year'] = dt.strptime(investment['fundedDate'], '%d-%b-%y').year
        except ValueError as err:
            stderr.write(f"Error occurred when trying to parse {investment['fundedDate']} to date:\n{err}\n")
        else:
            year_state_amount[(investment['year'], investment['state'])] += float(investment['raisedAmt'])
            year_state_cities[(investment['year'], investment['state'])].add(investment['city'])

    inv_stats = list()
    for year_state, inv_amount in year_state_amount.items():
        year, state = year_state
        inv_stats.append((year, state, inv_amount, len(year_state_cities[year_state])))

    inv_stats.sort(key=lambda s:(s[0], s[1]))

    write_to_csv(inv_stats, Path.cwd() / 'investment_stats.csv')


def write_to_csv(data, fpath):
    try:
        with open(fpath, 'w', newline='') as fobj:
            csv_writer = csv.writer(fobj)
            csv_writer.writerow(('year', 'state', 'tot_amount', 'city_count'))
            for data_row in data:
                csv_writer.writerow(data_row)
    except OSError as err:
        stderr.write("ERROR from csv writer of year_state_stats f.\n:{err}\n")


if __name__ == "__main__":

    investments_data = read_data_from_csv_v2(Path.cwd() / 'data' / 'techcrunch.csv')
    # for inv in investments_data:
    #     pprint(inv)
    #     print()

    # for inv_year, top_round_a_inv in sorted(highest_round_a_investments(investments_data).items()):
    #     company, amount = top_round_a_inv
    #     print(f"{inv_year}: {amount} by {company}")

    year_state_stats(investments_data)











