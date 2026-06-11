# python script for gene name conversions to ensembl
# need to convert all GEO file gene names to the same format
# choosing ensembl gene names for consistency
import mygene
import pandas as pd
# extract function from mygene:
mg = mygene.MyGeneInfo()

# list flattening function:
def flatten_with_first(lst):
    return [item[0] if isinstance(item, list) else item for item in lst]

# handles duplicates from symbol inputs:
def querymany_onetoone(mg, input_ids, scopes, fields, species):
    results = mg.querymany(input_ids, scopes=scopes, fields=fields, species=species)
    if scopes == "symbol":
        # deduplicate: build a dict keeping first hit per query, in input order
        result_map = {}
        for r in results:
            query = r['query']
            if query not in result_map:
                result_map[query] = r.get("ensembl")
        return [result_map.get(q) for q in input_ids]
    else:
        return [res.get("ensembl") for res in results]

# global vars:
inname="/path/to/in.csv"
outname="/path/to/out.csv"
sourcetype="entrezgene"
target_colname="GeneID"

# convert entrez IDs from GEO df:
df = pd.read_csv(inname)
input_ids = df[target_colname]
results = querymany_onetoone(mg, input_ids, scopes=sourcetype, fields="ensembl.gene", species="human")

# ensembl_list contains 3 distinct object types:
# (1) a single dict, such as: {'gene': 'ENSG00000310526'}
# (2) a nested list of dicts, such as: [{'gene': 'ENSG00000284557'}, {'gene': 'ENSG00000288468'}]
# (3) a character where no gene is found: "None"

# un-nest the lists:
ensembl_list = flatten_with_first(results)
# extract IDs from dict:
ensembl_list = [item['gene'] if item is not None else None for item in ensembl_list]

# add ensembl IDs back to df:
df['Ensembl'] = ensembl_list
# save:
df.to_csv(outname, index=False)