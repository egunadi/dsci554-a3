import pandas as pd
import math

def diameter_from_area(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    diameter = 2 * math.sqrt(area / math.pi)
    return diameter

def filter_data():
    filepath = '../data/SYB65_1_202209_Population, Surface Area and Density.csv'
        
    df = pd.read_csv(filepath, delimiter=',', encoding='utf-8')
        
    df = df.drop(columns='Region/Country/Area')
    df = df.rename(columns={'Unnamed: 1': 'Region/Country/Area'})
    
    popdensity22_df = df[(df['Series'] == 'Population density') & (df['Year'] == 2022)] 
    
    # find top ten countries with the greatest population density
    popdensity22_df['Value'] = popdensity22_df['Value'].replace(',', '', regex=True)
    popdensity22_df['Value'] = pd.to_numeric(popdensity22_df['Value'])
    popdensity22_df = popdensity22_df.sort_values(by='Value', ascending=False)
    
    # remove Region/Area entries
    popdensity22_df = popdensity22_df[~popdensity22_df['Region/Country/Area']
                                        .isin(['China, Macao SAR',
                                               'China, Hong Kong SAR',
                                               'Bermuda',
                                               'Holy See',
                                               'State of Palestine',
                                               'Mayotte',
                                               'Other non-specified areas'])]
    
    popdensity22_df = popdensity22_df.rename(columns={'Region/Country/Area': 'Country',
                                                      'Value': 'PopDensity22'})
    
    popdensity22_top10_df = popdensity22_df[['Country', 'PopDensity22']][:10]
    
    # calculate diameter for bubble cloud infographic
    popdensity22_top10_df['Diameter'] = popdensity22_top10_df['PopDensity22'] \
                                          .apply(diameter_from_area) \
                                          .astype('int')  
    
    popdensity22_top10_df.to_csv('../data/popdensity22_top10.csv', encoding='utf-8', index=False)

if __name__ == '__main__':
    filter_data()
