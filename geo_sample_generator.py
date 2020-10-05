import random
import pandas as pd
import datetime

# Function to generate spatial data
def generate_spatial_data(num_of_rows, lat_min, lat_max, lon_min, lon_max):
    samples = []
    i = 0
    while i < num_of_rows:
        sample = {}
        sample['id'] = i
        sample['lat'] = (lat_max - lat_min) * random.random() + lat_min
        sample['lon'] = (lon_max - lon_min) * random.random() + lon_min
        sample['rndm_measured_attr'] = random.randint(-140, -40)
        samples.append(sample)
        i += 1
    return samples

if __name__ == '__main__':
    # Define the number of samples and Bounding Box
    no_of_samples = 1000
    lat_min = 36.90
    lat_max = 48.08
    lon_min = -123
    lon_max = -115

    print('Start Time: {}'.format(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')))
    samples = generate_spatial_data(no_of_samples, lat_min, lat_max, lon_min, lon_max)
    samples_df = pd.DataFrame(samples)
    samples_df.to_csv('geo_samples.csv')
    print('File Generated: {}'.format('geo_samples.csv'))
    print('End Time: {}'.format(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')))