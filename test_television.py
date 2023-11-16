from television import Television  # Import the Television class

# Test Television class initialization
def test_television_initialization():
    tv = Television()
    assert tv._Television__status == False  # Test default status
    assert tv._Television__muted == False   # Test default mute status
    assert tv._Television__volume == 0      # Test default volume
    assert tv._Television__channel == 0     # Test default channel

# Test power method
def test_power_method():
    tv = Television()
    tv.power()
    assert tv._Television__status == True   
    tv.power()
    assert tv._Television__status == False  

# Test mute method
def test_mute_method():
    tv = Television()
    tv.mute()
    assert tv._Television__muted == True   
    tv.mute()
    assert tv._Television__muted == False   

# Test channel_up method
def test_channel_up_method():
    tv = Television()
    tv.power()  # Turning on TV to perform channel change
    tv.channel_up()
    assert tv._Television__channel == 1  # Test channel incremented when TV is on

# Test channel_down method
def test_channel_down_method():
    tv = Television()
    tv.power()  # Turning on TV to perform channel change
    tv.channel_down()
    assert tv._Television__channel == 3  # Test channel decremented when TV is on

# Test volume_up method
def test_volume_up_method():
    tv = Television()
    tv.power()  # Turning on TV to perform volume change
    tv.volume_up()
    assert tv._Television__volume == 1  # Test volume incremented when TV is on

# Test volume_down method
def test_volume_down_method():
    tv = Television()
    tv.power()  # Turning on TV to perform volume change
    tv.volume_down()
    assert tv._Television__volume == 0  # Test volume decremented when TV is on
