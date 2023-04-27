import csv
from faker import Faker
import os
import random

def generate_bids_path(participant_id, sessions, tasks, runs):
    # Validate input
    if not participant_id.startswith('sub-'):
        raise ValueError('participant_id is not in BIDS format')
    if not isinstance(sessions, int) or sessions < 1:
        raise ValueError('Invalid number of sessions')
    if not isinstance(tasks, int) or tasks < 1:
        raise ValueError('Invalid number of tasks')
    if not isinstance(runs, int) or runs < 1:
        raise ValueError('Invalid number of runs')
    
    # BIDS directory names and extensions
    bids_file_ext = 'nii.gz'

    # Generate file paths
    file_paths = []
    for j in range(sessions):
        session_id = f'ses-{j+1:02}'
        for k in range(tasks):
            task_id = f'task-{k+1:02}'
            for l in range(runs):
                run_id = f'run-{l+1:02}'
                path = '/'.join([participant_id, session_id, 'func'])
                path = '/'.join([path, f'{participant_id}_{session_id}_{task_id}_{run_id}_bold.{bids_file_ext}'])
                file_paths.append(path)
                    
    return file_paths

def generate_fake_csv(num_rows):
    # Generate fake data using Faker module
    fake = Faker()
    data = []
    for i in range(num_rows):
        age = fake.random_int(min=0, max=90)
        sex = random.choice(['F', 'M'])
        gender_identity = random.choice([
            'Agender',
            'Androgyne',
            'Androgynous',
            'Bigender',
            'Cis',
            'Cisgender',
            'Cis Female',
            'Cis Male',
            'Cis Man',
            'Cis Woman',
            'Cisgender Female',
            'Cisgender Male',
            'Cisgender Man',
            'Cisgender Woman',
            'Female to Male',
            'FTM',
            'Gender Fluid',
            'Gender Nonconforming',
            'Gender Questioning',
            'Gender Variant',
            'Genderqueer',
            'Intersex',
            'Male to Female',
            'MTF',
            'Neither',
            'Neutrois',
            'Non-binary',
            'Other',
            'Pangender',
            'Trans',
            'Trans*',
            'Trans Female',
            'Trans* Female',
            'Trans Male',
            'Trans* Male',
            'Trans Man',
            'Trans* Man',
            'Trans Person',
            'Trans* Person',
            'Trans Woman',
            'Trans* Woman',
            'Transfeminine',
            'Transgender',
            'Transgender Female',
            'Transgender Male',
            'Transgender Man',
            'Transgender Person',
            'Transgender Woman',
            'Transmasculine',
            'Transsexual',
            'Transsexual Female',
            'Transsexual Male',
            'Transsexual Man',
            'Transsexual Person',
            'Transsexual Woman',
            'Two-Spirit'
            ])
        pronouns = random.choice([
            'ae/aer',
            'e/em',
            'ey/em',
            'fae/faer',
            'he/him',
            'per/per',
            'she/her',
            'they/them',
            've/ver',
            'xe/xem',
            'ze/hir',
            'zie/hir'
            ])
        race = random.choice([
            'White',
            'Black or African American',
            'Asian',
            'Native American or Alaska Native',
            'Native Hawaiian or Other Pacific Islander',
            'Other'
            ])
        diagnosis = random.choice([
            'Neurodevelopmental Disorder',
            'Schizophrenia Spectrum or Other Psychotic Disorder',
            'Bipolar or Related Disorder',
            'Depressive Disorder',
            'Anxiety Disorder',
            'Obsessive-Compulsive or Related Disorder',
            'Trauma- or Stressor-Related Disorder',
            'Dissociative Disorder',
            'Somatic Symptom or Related Disorder',
            'Feeding or Eating Disorder',
            'Elimination Disorder',
            'Sleep-Wake Disorder',
            'Sexual Dysfunctions',
            'Gender Dysphoria',
            'Disruptive, Impulse-Control, or Conduct Disorder',
            'Substance-Related or Addictive Disorder',
            'Neurocognitive Disorder',
            'Personality Disorder',
            'Paraphilic Disorder',
            'Typical Control'
            ])
        zip_code = fake.zipcode()

        participant_id = f'sub-{i+1:05}'
        sessions = fake.random_int(min=1, max=3)
        tasks = fake.random_int(min=1, max=4)
        runs = fake.random_int(min=1, max=2)
        for file_path in generate_bids_path(participant_id, sessions, tasks, runs):
            data.append([participant_id, age, sex, diagnosis, gender_identity, pronouns, race, zip_code, file_path])

    # Write data to CSV file
    with open(os.path.join('data', 'fake_data.csv'), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['participant_id', 'age', 'sex', 'diagnosis', 'gender_identity', 'pronouns', 'race', 'zip_code', 'file_path'])
        writer.writerows(data)

generate_fake_csv(10000)
