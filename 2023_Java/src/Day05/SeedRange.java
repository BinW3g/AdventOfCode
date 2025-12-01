package Day05;

public class SeedRange {
    private long seed;
    private long range;
    private boolean allowChange = true;

    public SeedRange(long seed, long range) {
        this.seed = seed;
        this.range = range;
    }
    public SeedRange(String seed, String range) {
        this.seed = Long.parseLong(seed);
        this.range = Long.parseLong(range);
    }

    public long getSeed() {
        return seed;
    }

    public void setSeed(long seed) {
        this.seed = seed;
    }

    public long getRange() {
        return range;
    }

    public void setRange(long range) {
        this.range = range;
    }

    public boolean isAllowChange() {
        return allowChange;
    }



    public void setAllowChange(boolean allowChange) {
        this.allowChange = allowChange;
    }

    public SeedRange outOfRange(long maxRange){
        SeedRange newRange = new SeedRange(seed+maxRange, range-maxRange-1);
        range = maxRange;
        return newRange;
    }

    public SeedRange splitSeedAt(long splitPosition){
        SeedRange newRange = new SeedRange(seed,  Math.abs(splitPosition - seed)-1);
        range -= Math.abs(splitPosition - seed);
        seed = splitPosition;
        return newRange;
    }

    @Override
    public String toString() {
        return "SeedRange{" +
                "seed=" + seed +
                ", range=" + range +
                '}';
    }
}
