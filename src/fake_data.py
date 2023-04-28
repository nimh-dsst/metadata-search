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

        participant_id = f'sub-{i+1:05}'

        age = fake.random_int(min=0, max=90)

        sex = random.choice(['F', 'M'])

        gender = random.choice([
            "",
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
            "",
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
            "",
            'White',
            'Black or African American',
            'Asian',
            'Native American or Alaska Native',
            'Native Hawaiian or Other Pacific Islander',
            'Other'
            ])

        diagnosis = random.choice([
            "",
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

        study = random.choice([
            "GINA",
            "ADNI",
            "ISAAC",
            "CHARVA",
            "GOMETS",
            "GBD",
            "AGRE",
            "HapMap",
            "ICBP-GWAS",
            "PDBP",
            "GOLD",
            "IMSGC",
            "ICGC",
            "SHIP",
            "IGAP",
            "IIBDGC",
            "IHGC",
            "ILCCO",
            "CHS",
            "ISGC",
            "MMRF",
            "IEC",
            "DPPOS",
            "IPDGC",
            "SOF",
            "ICTME",
            "ICHR",
            "ICC-OHIA",
            "CSVD",
            "ILEC",
            "GCDD",
            "ICASA",
            "cVEDA",
            "iGeneTRAiN",
            "CPTDPs",
            "GCHCE",
            "ICCR",
            "ICGRTC",
            "GCPM",
            "CoMSSA",
            "ICBBB",
            "COTS",
            "CGHFBC",
            "GCCR",
            "CEGIR",
            "IEGC",
            "ICGCmed",
            "COGS",
            "iCLAHRC",
            "COGS"
            ])

        site = random.choice([
            "",
            "MIT",
            "Caltech",
            "Stanford",
            "Harvard",
            "Princeton",
            "Yale",
            "Oxford",
            "Cambridge",
            "Imperial College London",
            "University of Chicago",
            "Columbia",
            "University of California, Berkeley",
            "University of California, Los Angeles",
            "University of Michigan",
            "University of Texas at Austin",
            "University of Illinois at Urbana-Champaign",
            "University of Wisconsin-Madison",
            "University of Pennsylvania",
            "Duke",
            "Johns Hopkins",
            "Cornell",
            "Northwestern",
            "Brown",
            "University of Minnesota",
            "University of Washington",
            "University of North Carolina at Chapel Hill",
            "University of Colorado Boulder",
            "University of Arizona",
            "Arizona State University",
            "University of Utah",
            "University of California, San Diego",
            "University of Southern California",
            "University of Maryland, College Park",
            "Georgetown",
            "New York University",
            "University of Notre Dame",
            "University of Virginia",
            "Emory",
            "Rice",
            "University of Oregon",
            "Vanderbilt",
            "University of California, Davis",
            "University of Iowa",
            "University of Rochester",
            "University of California, Santa Barbara",
            "University of Pittsburgh",
            "University of Texas Southwestern Medical Center",
            "Washington University in St. Louis",
            "University of Toronto",
            "University of British Columbia",
            "McGill",
            "University of Alberta"
            ])

        has_mri = random.choice([True, False])
        has_meg = random.choice([True, False])
        has_eeg = random.choice([True, False])

        data.append([
            participant_id,
            study,
            site,
            age,
            sex,
            diagnosis,
            gender,
            pronouns,
            race,
            zip_code,
            has_mri,
            has_meg,
            has_eeg
            ])

        # sessions = fake.random_int(min=1, max=3)
        # tasks = fake.random_int(min=1, max=4)
        # runs = fake.random_int(min=1, max=2)
        # for file_path in generate_bids_path(participant_id, sessions, tasks, runs):
        #     data.append([
        #         study,
        #         participant_id,
        #         session_id,
        #         site,
        #         age,
        #         sex,
        #         diagnosis,
        #         gender,
        #         pronouns,
        #         race,
        #         zip_code,
        #         has_mri,
        #         has_meg,
        #         has_eeg,
        #         file_path
        #         ])

    # Write data to CSV file
    with open(os.path.join('data', 'fake_data.csv'), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "participant_id",
            "study",
            "site",
            "age",
            "sex",
            "diagnosis",
            "gender",
            "pronouns",
            "race",
            "zip_code",
            "has_mri",
            "has_meg",
            "has_eeg"
        ])
        writer.writerows(data)

generate_fake_csv(100000)

# need to figure out:
#   - phenotype data dictionary free text search
#   - do away with file_path
#   - session_id by either #s or individual names
#   - MRI sequence info
#   - not reported
#   - no/empty data
