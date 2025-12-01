package Day03;

public class MyInteger {
    private int integerValue = 0;

    public MyInteger(int m) {
        this.integerValue = m;
    }

    public int getIntegerValue() {
        return integerValue;
    }

    public void setIntegerValue(int integerValue) {
        this.integerValue = integerValue;
    }

    public void incrementValue(int increment) {
        integerValue += increment;
    }

    @Override
    public String toString() {
        return integerValue + "";
    }
}
