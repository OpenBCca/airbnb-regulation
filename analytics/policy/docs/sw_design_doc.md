# Software Design Doc

Status: Approved (2024-01-27)

Author: Nam Mai

Reviewer(s): Yang Su

## Context

To determine illegal rental listings on Airbnb, it is important to make sure business registry for each listing is validated. A system composed of policies and rules needs to be set up to effectively handle a large number of listings. 

## Scope

- Refer to short term rental legislation guidelines from BC and specific cities in Metro Vancouver
    - For starters, the following criteria will be assessed:
       - Valid registration number (uniqueness, expiration, status) (**MVP focus**)
       - Number of rental days (under 30 consecutive days is considered short-term)
       - Location (for example, Burnaby allows short-term rental for max 90 nights/year, Vancouver does not have this)
- Target only residential listings with registration number on Airbnb.

## Goals

- Validate listings by verifying info such as in Airbnb posts
- Apply appropriate rules/by-laws to properties in corresponding areas

## Non-goals

- Use other rental standards such as strata by-laws, strata council rules
- Categorize short-term and long-term rentals 
- Display PII with illegal listings
- Access homeowners' personal data

## Overview

The policy module takes listings from report module, applies and processes appropriate policies, and returns evaluated listings to the report module. It is designed to verify Airbnb listing in different criteria with sources from BC rental legislation and BC open service/database. 

## Detailed Design

The policy module contains policies that map to the corresponding Airbnb listing field. For the MVP, the objective is to verify each listing's license number. The license number status is determined by verifying matching license number (and house address) from a government official database, such as City of Vancouver Open Data Portal. Thus, a service/API handler is also needed in this module to call and pull data from the database. After processing the policies, the results are returned to the report module.

![image](https://github.com/OpenBCca/airbnb-regulation/assets/32988140/6f937155-af65-459a-8c9b-431a15c19f83)

The listing and policy mapping can be implemented with the Strategy Pattern, which focuses on isolating the policy for each listing info if we expand from registration number validation. The result object contains list of violation for each listing. Note that the API data layer is truncated in this diagram.

![image](https://github.com/OpenBCca/airbnb-regulation/assets/32988140/5b5d62af-f68f-4be4-891c-136121a868cd)

## Alternative Design

_TBD_

## Contracts

### Input from Report Module:
- Listing object with the following attributes:
	- Listing id
	- Listing address
	- Listing registration number

For MVP version, the above attributes are the focus. Other attributes such as Location, Number of rental days (per the diagram above) will be added in later stages.

### Output to Report Module:
- Results object:
	- List of violated policies

## Testing Methods

### Unit Testing

- Test each policy algorithm with defined inputs and expected outputs
- Test API endpoints for valid/invalid inputs for the policies

### Integration Testing

- Test API service integration with policies using mocking libraries
- Test API responses/error handling