package Day6;

public class RaceInfos {
    public int timeOfRace;
    public int distanceToWin;

    public RaceInfos(int timeOfRace) {
        this.timeOfRace = timeOfRace;
    }

    public RaceInfos(int timeOfRace, int distanceToWin) {
        this.timeOfRace = timeOfRace;
        this.distanceToWin = distanceToWin;
    }

    public int getTimeOfRace() {
        return timeOfRace;
    }

    public void setTimeOfRace(int timeOfRace) {
        this.timeOfRace = timeOfRace;
    }

    public int getDistanceToWin() {
        return distanceToWin;
    }

    public void setDistanceToWin(int distanceToWin) {
        this.distanceToWin = distanceToWin;
    }


}
