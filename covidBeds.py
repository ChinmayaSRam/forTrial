class City:
    def __init__(self, city_id, state_name, city_name, covidbeds, avlblcovbeds, ventilbeds, avlblventilbeds):
        self.city_id = city_id
        self.state_name = state_name
        self.city_name = city_name
        self.covidbeds = covidbeds
        self.avlblcovbeds = avlblcovbeds
        self.ventilbeds = ventilbeds
        self.avlblventilbeds = avlblventilbeds


class CovBedsAnalysis:
    def __init__(self, analysis_name, city_list):
        self.analysis_name = analysis_name
        self.city_list = city_list

    def get_StateWiseAvlblBedStats(self):
        state_stats = {}
        for city in self.city_list:
            state = city.state_name.lower()
            if state not in state_stats:
                state_stats[state] = [0, 0]  # Initialize total covid beds and total ventilator beds to 0
            state_stats[state][0] += city.avlblcovbeds
            state_stats[state][1] += city.avlblventilbeds

        # Convert state_stats to a list of tuples
        state_stats_list = [(state.capitalize(), beds[0], beds[1]) for state, beds in state_stats.items()]

        # Sort the list by state name
        state_stats_list.sort(key=lambda x: x[0])

        return state_stats_list

    def get_CiitesWithMoreThanAvgOccupiedbeds(self, state):
        state_cities = [city for city in self.city_list if city.state_name.lower() == state.lower()]
        if not state_cities:
            return None

        total_covid_beds = sum(city.covidbeds - city.avlblcovbeds for city in state_cities)
        total_ventil_beds = sum(city.ventilbeds - city.avlblventilbeds for city in state_cities)

        avg_covid_beds = total_covid_beds / len(state_cities)
        avg_ventil_beds = total_ventil_beds / len(state_cities)

        cities_with_more_beds = {}
        for city in state_cities:
            occupied_covid_beds = city.covidbeds - city.avlblcovbeds
            occupied_ventil_beds = city.ventilbeds - city.avlblventilbeds
            if occupied_covid_beds > avg_covid_beds and occupied_ventil_beds > avg_ventil_beds:
                cities_with_more_beds[city.city_name] = (occupied_covid_beds, occupied_ventil_beds)

        if not cities_with_more_beds:
            return None

        return cities_with_more_beds


def main():
    city_objects = []

    # Reading city data
    num_cities = int(input())
    for _ in range(num_cities):
        city_id = int(input())
        state_name = input()
        city_name = input()
        covidbeds = int(input())
        avlblcovbeds = int(input())
        ventilbeds = int(input())
        avlblventilbeds = int(input())

        city = City(city_id, state_name, city_name, covidbeds, avlblcovbeds, ventilbeds, avlblventilbeds)
        city_objects.append(city)

    analysis = CovBedsAnalysis('COVID-19 Beds Analysis', city_objects)

    # Get state-wise available bed statistics
    state_stats = analysis.get_StateWiseAvlblBedStats()
    for state, covid_beds, ventil_beds in state_stats:
        print(state, covid_beds, ventil_beds)

    # Get cities with more than average occupied beds
    state = input()
    city_beds = analysis.get_CiitesWithMoreThanAvgOccupiedbeds(state)
    if city_beds is None:
        print('No city available')
    else:
        for city, beds in city_beds.items():
            print(city, beds[0], beds[1])


if __name__ == '__main__':
    main()
