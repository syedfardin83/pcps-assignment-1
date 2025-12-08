import wx
import random


class GameApp:
    def __init__(self,app):
        # super().__init__(None, title="Game", size=(1000, 500))
        self.app  = app
        # Game state variables
        self.opponent_max_health = 100
        self.opponent_initial_health = 100
        self.opponent_health = self.opponent_initial_health
        self.opponent_attack_factor = 60
        self.opponent_heal_factor = 10
        
        self.player_max_health = 100
        self.player_initial_health = 100
        self.player_health = self.player_initial_health
        self.player_attack_factor = 60
        self.player_heal_factor = 10
        
        self.exit_game = False
        self.you_win = False
        self.you_lose = False
        
        # Window and image settings
        self.window_size = (1000, 500)
        self.bg_image_url = './images/forest_retro.png'
        self.player_image_url = './images/robin_hood.png'
        self.opp_image_url = './images/hunter.png'
        self.win_image_url = './images/you_win.png'
        self.lose_image_url = './images/you_lose.png'
        
        # Create UI
        self.frame = wx.Frame(None, title="Game", size=(1000, 500))
        self.panel = wx.Panel(self.frame, style=wx.SIMPLE_BORDER)
        self.panel.Bind(wx.EVT_PAINT, self.paint_all)
        
        # Create buttons using images
        self.attack_btn = wx.BitmapButton(self.panel, 
                                          bitmap=wx.Bitmap(wx.Image('./images/attack_button.png', wx.BITMAP_TYPE_ANY).Scale(100, 100)),
                                          pos=(self.window_size[0]-150, self.window_size[1]-150))
        self.attack_btn.Bind(wx.EVT_BUTTON, self.handle_attack)
        
        self.heal_btn = wx.BitmapButton(self.panel,
                                        bitmap=wx.Bitmap(wx.Image('./images/heal_button.png', wx.BITMAP_TYPE_ANY).Scale(100, 100)),
                                        pos=(self.window_size[0]-270, self.window_size[1]-150))
        self.heal_btn.Bind(wx.EVT_BUTTON, self.handle_heal)
        
        # Create restart button (initially hidden)
        self.restart_btn = wx.BitmapButton(self.panel,
                                           bitmap=wx.Bitmap(wx.Image('./images/restart.png', wx.BITMAP_TYPE_ANY).Scale(160, 80)),
                                           pos=(410, self.window_size[1]-150))
        self.restart_btn.Bind(wx.EVT_BUTTON, self.handle_restart)
        self.restart_btn.Hide()
        
        # Create health text displays
        self.player_health_text = wx.StaticText(self.panel, label=f"SELF HEALTH: {self.player_health}", 
                                                pos=(self.window_size[0]-330, 60))
        self.player_health_text.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, 
                                                wx.FONTWEIGHT_BOLD))
        self.player_health_text.SetForegroundColour(wx.Colour(0, 0, 0))
        
        self.opponent_health_text = wx.StaticText(self.panel, label=f"OPPONENT HEALTH: {self.opponent_health}", 
                                                  pos=(30, 60))
        self.opponent_health_text.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, 
                                                  wx.FONTWEIGHT_BOLD))
        self.opponent_health_text.SetForegroundColour(wx.Colour(0, 0, 0))
        self.frame.Show()
    def update_health_displays(self):
        """Update the health text displays"""
        self.player_health_text.SetLabel(f"SELF HEALTH: {self.player_health}")
        self.opponent_health_text.SetLabel(f"OPPONENT HEALTH: {self.opponent_health}")
        self.panel.Refresh()
    
    def handle_attack(self, event):
        if self.you_win or self.you_lose:
            return
            
        print("Attack Button clicked!!")
        print("\n***** ATTACKING... ****")
        player_attack = int(random.random() * self.player_attack_factor)
        opponent_attack = int(random.random() * self.opponent_attack_factor)
        net_attack = player_attack - opponent_attack
        print(f'Attack amount: {player_attack}\nOpponent attack amount: {opponent_attack}\nEffective Attack: {net_attack}')
        
        if net_attack < 0:
            print(f"\n*** Opponent successfully defended your attack ***\n****  You dealt damage of {-1*net_attack} ****")
            if not (self.player_health + net_attack < 0):
                self.player_health += net_attack
            else:
                print("You LOST!")
                self.you_lose = True
                self.player_health = 0
                self.show_game_over()
        else:
            print(f"\n****  Opponent dealt damage of {net_attack} ****")
            if not (self.opponent_health - net_attack < 0):
                self.opponent_health -= net_attack
            else:
                print("You Win!")
                self.opponent_health = 0
                self.you_win = True
                self.show_game_over()
        
        self.update_health_displays()
    
    def handle_heal(self, event):
        if self.you_win or self.you_lose:
            return
            
        print("Heal button clicked!")
        print("\n***** HEALING... ****")
        player_heal = int(random.random() * self.player_heal_factor)
        opponent_heal = int(random.random() * self.opponent_heal_factor)
        
        if not (player_heal + self.player_health > self.player_max_health):
            self.player_health += player_heal
        else:
            self.player_health = self.player_max_health
        
        if not (opponent_heal + self.opponent_health > self.opponent_max_health):
            self.opponent_health += opponent_heal
        else:
            self.opponent_health = self.opponent_max_health
        
        print(f"\nYou healed by {player_heal}\nOpponent healed by {opponent_heal}")
        self.update_health_displays()
    
    def show_game_over(self):
        """Show win/lose message box and restart button"""
        if self.you_win:
            wx.MessageBox("Congratulations! You Won!", "Victory", wx.OK | wx.ICON_INFORMATION)
        elif self.you_lose:
            wx.MessageBox("Game Over! You Lost!", "Defeat", wx.OK | wx.ICON_INFORMATION)
        
        # Show restart button
        self.restart_btn.Show()
        self.panel.Refresh()
    
    def handle_restart(self, event):
        """Reset the game"""
        print("Restarting game...")
        self.you_win = False
        self.you_lose = False
        self.player_health = self.player_initial_health
        self.opponent_health = self.opponent_initial_health
        
        # Hide restart button
        self.restart_btn.Hide()
        
        # Update displays
        self.update_health_displays()
    
    def paint_all(self, event):
        dc = wx.PaintDC(self.panel)
        
        # Draw background
        bg_bitmap = wx.Bitmap(wx.Image(self.bg_image_url, wx.BITMAP_TYPE_ANY).Scale(self.window_size[0], self.window_size[1]))
        dc.DrawBitmap(bg_bitmap, 0, 0)
        
        # Draw opponent (scaled to match pygame)
        opp_bitmap = wx.Bitmap(wx.Image(self.opp_image_url, wx.BITMAP_TYPE_ANY).Scale(200, 200))
        dc.DrawBitmap(opp_bitmap, 100, self.window_size[1]-400, True)
        
        # Draw player (scaled to match pygame)
        player_bitmap = wx.Bitmap(wx.Image(self.player_image_url, wx.BITMAP_TYPE_ANY).Scale(100, 200))
        dc.DrawBitmap(player_bitmap, self.window_size[0]-150, self.window_size[1]-400, True)
        
        # Draw win/lose image if game is over
        if self.you_win:
            win_bitmap = wx.Bitmap(wx.Image(self.win_image_url, wx.BITMAP_TYPE_ANY).Scale(400, 120))
            dc.DrawBitmap(win_bitmap, 320, 200, True)
        
        if self.you_lose:
            lose_bitmap = wx.Bitmap(wx.Image(self.lose_image_url, wx.BITMAP_TYPE_ANY).Scale(400, 120))
            dc.DrawBitmap(lose_bitmap, 320, 200, True)


if __name__ == '__main__':
    print("Starting!")
    app = wx.App()
    a=GameApp(app)
    app.MainLoop()