import json


def prepare_share_and_fund_ID():
    shareID_to_lookupID = {}
    fundID_to_lookupID = {}
    with open("ID_MAPPING.txt") as f:
        for line in f:
            v2_lookup_id, share_class_id, fund_class_id = line.strip().split('	', 2)
            if share_class_id in shareID_to_lookupID.keys():
                shareID_to_lookupID[share_class_id].append(v2_lookup_id)
            else:
                shareID_to_lookupID[share_class_id] = [v2_lookup_id]
            if fund_class_id in fundID_to_lookupID.keys():
                fundID_to_lookupID[fund_class_id].append(v2_lookup_id)
            else:
                fundID_to_lookupID[fund_class_id] = [v2_lookup_id]
    f.close()

    with open("shareID_list.txt", "w") as f:
        f.write('\n'.join(id for id in shareID_to_lookupID.keys()))
    f.close()

    with open("shareID_to_lookupID.json", "w") as f:
        json.dump(shareID_to_lookupID, f)
    f.close()

    with open("fundID_list.txt", "w") as f:
        f.write('\n'.join(id for id in fundID_to_lookupID.keys()))
    f.close()

    with open("fundID_to_lookupID.json", "w") as f:
        json.dump(fundID_to_lookupID, f)
    f.close()


def prepare_portfolioID():
    portfolioID_to_lookupID = {}
    with open("Perf_PortfolioId_mapping.txt") as f:
        for line in f:
            v2_lookup_id, portfolioID = line.strip().split('	', 2)
            portfolioID = portfolioID.replace(',', '')
            if portfolioID == "[NULL]":
                continue
            if portfolioID in portfolioID_to_lookupID.keys():
                portfolioID_to_lookupID[portfolioID].append(v2_lookup_id)
            else:
                portfolioID_to_lookupID[portfolioID] = [v2_lookup_id]
    f.close()

    with open("PortfolioID_list.txt", "w") as f:
        f.write('\n'.join(id for id in portfolioID_to_lookupID.keys()))
    f.close()

    with open("PerfID_to_lookupID.json", "w") as f:
        json.dump(portfolioID_to_lookupID, f)
    f.close()


if __name__ == "__main__":
    prepare_share_and_fund_ID()
    prepare_portfolioID()
