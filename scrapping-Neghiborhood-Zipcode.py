import pandas as pd

# mapping از سایت spyglassrealty و منابع دیگه (کامل‌تر از قبلی)
zip_to_neighborhood = {
    '78701': 'Downtown Austin',
    '78702': 'East Austin',
    '78703': 'Tarrytown, Clarksville',
    '78704': 'South Lamar, Zilker, Bouldin Creek, Travis Heights',
    '78705': 'North University, Hyde Park',
    '78717': 'Avery Ranch',
    '78721': 'East Austin',
    '78722': 'Cherrywood',
    '78723': 'Mueller, Windsor Park',
    '78724': 'East Austin',
    '78725': 'Hornsby Bend',
    '78726': 'Four Points',
    '78727': 'North Austin',
    '78728': 'Wells Branch',
    '78729': 'Jollyville',
    '78730': 'River Place',
    '78731': 'Northwest Hills',
    '78732': 'Steiner Ranch',
    '78733': 'Westlake',
    '78735': 'Oak Hill',
    '78736': 'Oak Hill',
    '78737': 'Dripping Springs area',
    '78738': 'Lakeway',
    '78739': 'Circle C',
    '78741': 'Riverside, Montopolis',
    '78742': 'Southeast Austin',
    '78744': 'Southeast Austin',
    '78745': 'South Austin, Garrison Park',
    '78746': 'West Lake Hills, Rollingwood',
    '78747': 'South Austin',
    '78748': 'South Austin',
    '78749': 'Circle C, Oak Hill',
    '78750': 'Anderson Mill',
    '78751': 'Hyde Park',
    '78752': 'North Loop',
    '78753': 'North Austin',
    '78754': 'Pioneer Crossing',
    '78756': 'Rosedale',
    '78757': 'Allandale, Crestview',
    '78758': 'North Austin',
    '78759': 'Arboretum, Great Hills'
}

mapping_df = pd.DataFrame(list(zip_to_neighborhood.items()), columns=['ZIP_Code', 'Neighborhood'])
mapping_df.to_csv('austin_zip_to_neighborhood_full.csv', index=False)

print("mapping جدید آماده!")
print(mapping_df.head(20))