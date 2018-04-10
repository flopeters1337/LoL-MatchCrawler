
import os
import json
import requests
import random

metadata_names = [
    'seasonId',
    'queueId',
    'gameVersion'
]

team_data_names = [
    'firstDragon',
    'firstInhibitor',
    'baronKills',
    'firstRiftHerald',
    'firstBaron',
    'riftHeraldKills',
    'firstBlood',
    'firstTower',
    'inhibitorKills',
    'towerKills',
    'win',
    'dragonKills'
]

player_data_names = [
    'lane',
    'role'
]

player_stats_names = [
    'physicalDamageDealt',
    'neutralMinionsKilledTeamJungle',
    'magicDamageDealt',
    'totalPlayerScore',
    'deaths',
    'win',
    'neutralMinionsKilledEnemyJungle',
    'totalDamageDealt',
    'magicDamageDealtToChampions',
    'damageDealtToObjectives',
    'totalTimeCrowdControlDealt',
    'longestTimeSpentLiving',
    'firstTowerAssist',
    'firstTowerKill',
    'firstBloodAssist',
    'turretKills',
    'damageSelfMitigated',
    'firstInhibitorKill',
    'magicalDamageTaken',
    'kills',
    'trueDamageTaken',
    'firstInhibitorAssist',
    'assists',
    'objectivePlayerScore',
    'combatPlayerScore',
    'damageDealtToTurrets',
    'physicalDamageDealtToChampions',
    'trueDamageDealt',
    'trueDamageDealtToChampions',
    'totalHeal',
    'firstBloodKill',
    'totalDamageDealtToChampions',
    'totalUnitsHealed',
    'inhibitorKills',
    'totalDamageTaken',
    'timeCCingOthers',
    'physicalDamageTaken'
]

column_names = [
    'seasonId',
    'queueId',
    'gameVersion',

    'firstDragon_team1',
    'firstInhibitor_team1',
    'baronKills_team1',
    'firstRiftHerald_team1',
    'firstBaron_team1',
    'riftHeraldKills_team1',
    'firstBlood_team1',
    'firstTower_team1',
    'inhibitorKills_team1',
    'towerKills_team1',
    'win_team1',
    'dragonKills_team1',
    'championIdBanTurn1_team1',
    'championIdBanTurn2_team1',
    'championIdBanTurn3_team1',
    'championIdBanTurn4_team1',
    'championIdBanTurn5_team1',

    'firstDragon_team2',
    'firstInhibitor_team2',
    'baronKills_team2',
    'firstRiftHerald_team2',
    'firstBaron_team2',
    'riftHeraldKills_team2',
    'firstBlood_team2',
    'firstTower_team2',
    'inhibitorKills_team2',
    'towerKills_team2',
    'win_team2',
    'dragonKills_team2',
    'championIdBanTurn6_team2',
    'championIdBanTurn7_team2',
    'championIdBanTurn8_team2',
    'championIdBanTurn9_team2',
    'championIdBanTurn10_team2',

    'championId_player1',
    'lane_player1',
    'role_player1',
    'physicalDamageDealt_player1',
    'neutralMinionsKilledTeamJungle_player1',
    'magicDamageDealt_player1',
    'totalPlayerScore_player1',
    'deaths_player1',
    'win_player1',
    'neutralMinionsKilledEnemyJungle_player1',
    'totalDamageDealt_player1',
    'magicDamageDealtToChampions_player1',
    'damageDealtToObjectives_player1',
    'totalTimeCrowdControlDealt_player1',
    'longestTimeSpentLiving_player1',
    'firstTowerAssist_player1',
    'firstTowerKill_player1',
    'firstBloodAssist_player1',
    'turretKills_player1',
    'damageSelfMitigated_player1',
    'firstInhibitorKill_player1',
    'magicalDamageTaken_player1',
    'kills_player1',
    'trueDamageTaken_player1',
    'firstInhibitorAssist_player1',
    'assists_player1',
    'objectivePlayerScore_player1',
    'combatPlayerScore_player1',
    'damageDealtToTurrets_player1',
    'physicalDamageDealtToChampions_player1',
    'trueDamageDealt_player1',
    'trueDamageDealtToChampions_player1',
    'totalHeal_player1',
    'firstBloodKill_player1',
    'totalDamageDealtToChampions_player1',
    'totalUnitsHealed_player1',
    'inhibitorKills_player1',
    'totalDamageTaken_player1',
    'timeCCingOthers_player1',
    'physicalDamageTaken_player1',

    'championId_player2',
    'lane_player2',
    'role_player2',
    'physicalDamageDealt_player2',
    'neutralMinionsKilledTeamJungle_player2',
    'magicDamageDealt_player2',
    'totalPlayerScore_player2',
    'deaths_player2',
    'win_player2',
    'neutralMinionsKilledEnemyJungle_player2',
    'totalDamageDealt_player2',
    'magicDamageDealtToChampions_player2',
    'damageDealtToObjectives_player2',
    'totalTimeCrowdControlDealt_player2',
    'longestTimeSpentLiving_player2',
    'firstTowerAssist_player2',
    'firstTowerKill_player2',
    'firstBloodAssist_player2',
    'turretKills_player2',
    'damageSelfMitigated_player2',
    'firstInhibitorKill_player2',
    'magicalDamageTaken_player2',
    'kills_player2',
    'trueDamageTaken_player2',
    'firstInhibitorAssist_player2',
    'assists_player2',
    'objectivePlayerScore_player2',
    'combatPlayerScore_player2',
    'damageDealtToTurrets_player2',
    'physicalDamageDealtToChampions_player2',
    'trueDamageDealt_player2',
    'trueDamageDealtToChampions_player2',
    'totalHeal_player2',
    'firstBloodKill_player2',
    'totalDamageDealtToChampions_player2',
    'totalUnitsHealed_player2',
    'inhibitorKills_player2',
    'totalDamageTaken_player2',
    'timeCCingOthers_player2',
    'physicalDamageTaken_player2',

    'championId_player3',
    'lane_player3',
    'role_player3',
    'physicalDamageDealt_player3',
    'neutralMinionsKilledTeamJungle_player3',
    'magicDamageDealt_player3',
    'totalPlayerScore_player3',
    'deaths_player3',
    'win_player3',
    'neutralMinionsKilledEnemyJungle_player3',
    'totalDamageDealt_player3',
    'magicDamageDealtToChampions_player3',
    'damageDealtToObjectives_player3',
    'totalTimeCrowdControlDealt_player3',
    'longestTimeSpentLiving_player3',
    'firstTowerAssist_player3',
    'firstTowerKill_player3',
    'firstBloodAssist_player3',
    'turretKills_player3',
    'damageSelfMitigated_player3',
    'firstInhibitorKill_player3',
    'magicalDamageTaken_player3',
    'kills_player3',
    'trueDamageTaken_player3',
    'firstInhibitorAssist_player3',
    'assists_player3',
    'objectivePlayerScore_player3',
    'combatPlayerScore_player3',
    'damageDealtToTurrets_player3',
    'physicalDamageDealtToChampions_player3',
    'trueDamageDealt_player3',
    'trueDamageDealtToChampions_player3',
    'totalHeal_player3',
    'firstBloodKill_player3',
    'totalDamageDealtToChampions_player3',
    'totalUnitsHealed_player3',
    'inhibitorKills_player3',
    'totalDamageTaken_player3',
    'timeCCingOthers_player3',
    'physicalDamageTaken_player3',

    'championId_player4',
    'lane_player4',
    'role_player4',
    'physicalDamageDealt_player4',
    'neutralMinionsKilledTeamJungle_player4',
    'magicDamageDealt_player4',
    'totalPlayerScore_player4',
    'deaths_player4',
    'win_player4',
    'neutralMinionsKilledEnemyJungle_player4',
    'totalDamageDealt_player4',
    'magicDamageDealtToChampions_player4',
    'damageDealtToObjectives_player4',
    'totalTimeCrowdControlDealt_player4',
    'longestTimeSpentLiving_player4',
    'firstTowerAssist_player4',
    'firstTowerKill_player4',
    'firstBloodAssist_player4',
    'turretKills_player4',
    'damageSelfMitigated_player4',
    'firstInhibitorKill_player4',
    'magicalDamageTaken_player4',
    'kills_player4',
    'trueDamageTaken_player4',
    'firstInhibitorAssist_player4',
    'assists_player4',
    'objectivePlayerScore_player4',
    'combatPlayerScore_player4',
    'damageDealtToTurrets_player4',
    'physicalDamageDealtToChampions_player4',
    'trueDamageDealt_player4',
    'trueDamageDealtToChampions_player4',
    'totalHeal_player4',
    'firstBloodKill_player4',
    'totalDamageDealtToChampions_player4',
    'totalUnitsHealed_player4',
    'inhibitorKills_player4',
    'totalDamageTaken_player4',
    'timeCCingOthers_player4',
    'physicalDamageTaken_player4',

    'championId_player5',
    'lane_player5',
    'role_player5',
    'physicalDamageDealt_player5',
    'neutralMinionsKilledTeamJungle_player5',
    'magicDamageDealt_player5',
    'totalPlayerScore_player5',
    'deaths_player5',
    'win_player5',
    'neutralMinionsKilledEnemyJungle_player5',
    'totalDamageDealt_player5',
    'magicDamageDealtToChampions_player5',
    'damageDealtToObjectives_player5',
    'totalTimeCrowdControlDealt_player5',
    'longestTimeSpentLiving_player5',
    'firstTowerAssist_player5',
    'firstTowerKill_player5',
    'firstBloodAssist_player5',
    'turretKills_player5',
    'damageSelfMitigated_player5',
    'firstInhibitorKill_player5',
    'magicalDamageTaken_player5',
    'kills_player5',
    'trueDamageTaken_player5',
    'firstInhibitorAssist_player5',
    'assists_player5',
    'objectivePlayerScore_player5',
    'combatPlayerScore_player5',
    'damageDealtToTurrets_player5',
    'physicalDamageDealtToChampions_player5',
    'trueDamageDealt_player5',
    'trueDamageDealtToChampions_player5',
    'totalHeal_player5',
    'firstBloodKill_player5',
    'totalDamageDealtToChampions_player5',
    'totalUnitsHealed_player5',
    'inhibitorKills_player5',
    'totalDamageTaken_player5',
    'timeCCingOthers_player5',
    'physicalDamageTaken_player5',

    'championId_player6',
    'lane_player6',
    'role_player6',
    'physicalDamageDealt_player6',
    'neutralMinionsKilledTeamJungle_player6',
    'magicDamageDealt_player6',
    'totalPlayerScore_player6',
    'deaths_player6',
    'win_player6',
    'neutralMinionsKilledEnemyJungle_player6',
    'totalDamageDealt_player6',
    'magicDamageDealtToChampions_player6',
    'damageDealtToObjectives_player6',
    'totalTimeCrowdControlDealt_player6',
    'longestTimeSpentLiving_player6',
    'firstTowerAssist_player6',
    'firstTowerKill_player6',
    'firstBloodAssist_player6',
    'turretKills_player6',
    'damageSelfMitigated_player6',
    'firstInhibitorKill_player6',
    'magicalDamageTaken_player6',
    'kills_player6',
    'trueDamageTaken_player6',
    'firstInhibitorAssist_player6',
    'assists_player6',
    'objectivePlayerScore_player6',
    'combatPlayerScore_player6',
    'damageDealtToTurrets_player6',
    'physicalDamageDealtToChampions_player6',
    'trueDamageDealt_player6',
    'trueDamageDealtToChampions_player6',
    'totalHeal_player6',
    'firstBloodKill_player6',
    'totalDamageDealtToChampions_player6',
    'totalUnitsHealed_player6',
    'inhibitorKills_player6',
    'totalDamageTaken_player6',
    'timeCCingOthers_player6',
    'physicalDamageTaken_player6',

    'championId_player7',
    'lane_player7',
    'role_player7',
    'physicalDamageDealt_player7',
    'neutralMinionsKilledTeamJungle_player7',
    'magicDamageDealt_player7',
    'totalPlayerScore_player7',
    'deaths_player7',
    'win_player7',
    'neutralMinionsKilledEnemyJungle_player7',
    'totalDamageDealt_player7',
    'magicDamageDealtToChampions_player7',
    'damageDealtToObjectives_player7',
    'totalTimeCrowdControlDealt_player7',
    'longestTimeSpentLiving_player7',
    'firstTowerAssist_player7',
    'firstTowerKill_player7',
    'firstBloodAssist_player7',
    'turretKills_player7',
    'damageSelfMitigated_player7',
    'firstInhibitorKill_player7',
    'magicalDamageTaken_player7',
    'kills_player7',
    'trueDamageTaken_player7',
    'firstInhibitorAssist_player7',
    'assists_player7',
    'objectivePlayerScore_player7',
    'combatPlayerScore_player7',
    'damageDealtToTurrets_player7',
    'physicalDamageDealtToChampions_player7',
    'trueDamageDealt_player7',
    'trueDamageDealtToChampions_player7',
    'totalHeal_player7',
    'firstBloodKill_player7',
    'totalDamageDealtToChampions_player7',
    'totalUnitsHealed_player7',
    'inhibitorKills_player7',
    'totalDamageTaken_player7',
    'timeCCingOthers_player7',
    'physicalDamageTaken_player7',

    'championId_player8',
    'lane_player8',
    'role_player8',
    'physicalDamageDealt_player8',
    'neutralMinionsKilledTeamJungle_player8',
    'magicDamageDealt_player8',
    'totalPlayerScore_player8',
    'deaths_player8',
    'win_player8',
    'neutralMinionsKilledEnemyJungle_player8',
    'totalDamageDealt_player8',
    'magicDamageDealtToChampions_player8',
    'damageDealtToObjectives_player8',
    'totalTimeCrowdControlDealt_player8',
    'longestTimeSpentLiving_player8',
    'firstTowerAssist_player8',
    'firstTowerKill_player8',
    'firstBloodAssist_player8',
    'turretKills_player8',
    'damageSelfMitigated_player8',
    'firstInhibitorKill_player8',
    'magicalDamageTaken_player8',
    'kills_player8',
    'trueDamageTaken_player8',
    'firstInhibitorAssist_player8',
    'assists_player8',
    'objectivePlayerScore_player8',
    'combatPlayerScore_player8',
    'damageDealtToTurrets_player8',
    'physicalDamageDealtToChampions_player8',
    'trueDamageDealt_player8',
    'trueDamageDealtToChampions_player8',
    'totalHeal_player8',
    'firstBloodKill_player8',
    'totalDamageDealtToChampions_player8',
    'totalUnitsHealed_player8',
    'inhibitorKills_player8',
    'totalDamageTaken_player8',
    'timeCCingOthers_player8',
    'physicalDamageTaken_player8',

    'championId_player9',
    'lane_player9',
    'role_player9',
    'physicalDamageDealt_player9',
    'neutralMinionsKilledTeamJungle_player9',
    'magicDamageDealt_player9',
    'totalPlayerScore_player9',
    'deaths_player9',
    'win_player9',
    'neutralMinionsKilledEnemyJungle_player9',
    'totalDamageDealt_player9',
    'magicDamageDealtToChampions_player9',
    'damageDealtToObjectives_player9',
    'totalTimeCrowdControlDealt_player9',
    'longestTimeSpentLiving_player9',
    'firstTowerAssist_player9',
    'firstTowerKill_player9',
    'firstBloodAssist_player9',
    'turretKills_player9',
    'damageSelfMitigated_player9',
    'firstInhibitorKill_player9',
    'magicalDamageTaken_player9',
    'kills_player9',
    'trueDamageTaken_player9',
    'firstInhibitorAssist_player9',
    'assists_player9',
    'objectivePlayerScore_player9',
    'combatPlayerScore_player9',
    'damageDealtToTurrets_player9',
    'physicalDamageDealtToChampions_player9',
    'trueDamageDealt_player9',
    'trueDamageDealtToChampions_player9',
    'totalHeal_player9',
    'firstBloodKill_player9',
    'totalDamageDealtToChampions_player9',
    'totalUnitsHealed_player9',
    'inhibitorKills_player9',
    'totalDamageTaken_player9',
    'timeCCingOthers_player9',
    'physicalDamageTaken_player9',

    'championId_player10',
    'lane_player10',
    'role_player10',
    'physicalDamageDealt_player10',
    'neutralMinionsKilledTeamJungle_player10',
    'magicDamageDealt_player10',
    'totalPlayerScore_player10',
    'deaths_player10',
    'win_player10',
    'neutralMinionsKilledEnemyJungle_player10',
    'totalDamageDealt_player10',
    'magicDamageDealtToChampions_player10',
    'damageDealtToObjectives_player10',
    'totalTimeCrowdControlDealt_player10',
    'longestTimeSpentLiving_player10',
    'firstTowerAssist_player10',
    'firstTowerKill_player10',
    'firstBloodAssist_player10',
    'turretKills_player10',
    'damageSelfMitigated_player10',
    'firstInhibitorKill_player10',
    'magicalDamageTaken_player10',
    'kills_player10',
    'trueDamageTaken_player10',
    'firstInhibitorAssist_player10',
    'assists_player10',
    'objectivePlayerScore_player10',
    'combatPlayerScore_player10',
    'damageDealtToTurrets_player10',
    'physicalDamageDealtToChampions_player10',
    'trueDamageDealt_player10',
    'trueDamageDealtToChampions_player10',
    'totalHeal_player10',
    'firstBloodKill_player10',
    'totalDamageDealtToChampions_player10',
    'totalUnitsHealed_player10',
    'inhibitorKills_player10',
    'totalDamageTaken_player10',
    'timeCCingOthers_player10',
    'physicalDamageTaken_player10'
]


class LoLCrawler:
    def __init__(self,
                 riot_key: str,
                 riot_server: str = 'https://na1.api.riotgames.com'):
        """Default constructor

        :param riot_key:    A valid Riot Games API key.
        :param riot_server: Riot server address.
        """
        self.__api_key = riot_key
        self.__riot_server = riot_server
        self.__seen_matches = set()
        self.__summoners_set = set()

    def crawl(self, seed_summoner_id: int, queue: int = 420, season: int = 11,
              output_file=os.path.join('data', 'crawled-data.csv')):
        """Crawl Riot Games' API to fetch matches' data.

        :param seed_summoner_id:    A seed summoner id to bootstrap the
                                    crawling process.
        :param queue:
        :param season:
        :param output_file:         A filepath to store the parsed data.
        :return:    Crawls through Riot Games' API starting from the recent
                    matches of the required summoner. The crawler uses summoner
                    ids from the matches to recursively search recent matches
                    of theirs too.
        """
        # Create output file if it does not already exist
        if not os.path.isfile(output_file):
            if not os.path.isdir(os.path.dirname(output_file)):
                os.mkdir(os.path.dirname(output_file))

            with open(output_file, mode='w') as output:
                output.write(','.join(column_names) + '\n')

        # Initialize summoners set
        self.__summoners_set.add(seed_summoner_id)

        while True:
            # Select random summoner ID from the summoners' set
            curr_summoner_id = random.choice(list(self.__summoners_set))
            self.__summoners_set.remove(curr_summoner_id)

            # Get matches list for the current summoner
            params = {
                        "api_key": self.__api_key,
                        "queue": queue,
                        "season": season,
                        "beginIndex": 0,
                        "endIndex": 20
                     }
            response = requests.get(self.__riot_server
                                    + '/lol/match/v3/matchlists/by-account/'
                                    + str(curr_summoner_id),
                                    params)
            if not response.ok:
                raise RuntimeError('Request failed with error code ' +
                                   str(response.status_code))

            api_response = json.loads(response.text)

            # Aggregate matches' ID
            matches = set()
            for i in range(0, min(api_response['totalGames'],
                                  params['endIndex'])):
                matches.add(api_response['matches'][i]['gameId'])

            # Remove matches we've already seen to prevent duplicates
            matches = matches - self.__seen_matches

            # Fetch match data
            for match_id in matches:
                response = requests.get(self.__riot_server
                                        + '/lol/match/v3/matches/'
                                        + str(match_id),
                                        {'api_key': self.__api_key})
                if not response.ok:
                    raise RuntimeError('Request failed with error code ' +
                                       str(response.status_code))

                json_data = json.loads(response.text)
                new_data = list()

                # Get match metadata
                for metadata in metadata_names:
                    new_data.append(json_data[metadata])

                # Get both teams' statistics
                for team_num in range(0, 2):
                    for team_data in team_data_names:
                        new_data.append(json_data['teams']
                                        [team_num][team_data])

                    # Get champion bans
                    for ban in range(0, 5):
                        new_data.append(json_data['teams']
                                        [team_num]['bans'][ban]['championId'])

                # Get each players' statistics
                for player_num in range(0, 10):
                    new_data.append(json_data['participants']
                                    [player_num]['championId'])
                    for player_data in player_data_names:
                        new_data.append(json_data['participants']
                                        [player_num]['timeline'][player_data])
                    for player_stat in player_stats_names:
                        stats = json_data['participants'][player_num]['stats']
                        if player_stat in stats.keys():
                            new_data.append(json_data['participants']
                                            [player_num]['stats'][player_stat])
                        else:
                            new_data.append(-1)

                # Add new data to the output file
                fetched_data_string = ','.join([str(x) for x in new_data]) \
                                      + '\n'
                with open(output_file, mode='a') as output:
                    output.write(fetched_data_string)

                # Add match's summoners' ids to the set of summoners
                for i in range(0, 10):
                    summoner_id = json_data['participantIdentities'][i]['player']['accountId']
                    if summoner_id != curr_summoner_id:
                        self.__summoners_set.add(summoner_id)

                # Add match_id to set of seen matches
                self.__seen_matches.add(match_id)
