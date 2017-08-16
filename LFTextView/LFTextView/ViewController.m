//
//  ViewController.m
//  LFTextView
//
//  Created by 刘飞 on 2017/8/11.
//  Copyright © 2017年 刘飞. All rights reserved.
//

#import "ViewController.h"


#define ScreenWidth [UIScreen mainScreen].bounds.size.width
#define ScreenHeight [UIScreen mainScreen].bounds.size.height

@interface ViewController ()<UITextViewDelegate, UIScrollViewDelegate, UITableViewDelegate, UITableViewDataSource>


@property (nonatomic, strong) UIScrollView *mainScrollView;

@property (nonatomic, strong) UIView *bannerView;

@property (nonatomic, strong) UITableView *talentTableView;

@property (nonatomic, strong) UITableView *friendTableView;

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.automaticallyAdjustsScrollViewInsets = NO;
    
    [self creatUI];
    
}


-(void)creatUI {
    
    [self.view addSubview:self.mainScrollView];
    [self.mainScrollView addSubview:self.bannerView];
    [self.mainScrollView addSubview:self.talentTableView];
    
    
    
    
//    [self.view addSubview:self.friendTableView];
}


-(void)scrollViewDidScroll:(UIScrollView *)scrollView {
    
    
    
    if (scrollView == self.mainScrollView) {
        NSLog(@"scrollview:%f", self.mainScrollView.contentOffset.y);
        if (self.mainScrollView.contentOffset.y >= 175) {
            NSLog(@"头部视图滚到顶部了");
            self.talentTableView.scrollEnabled = YES;
        }
    }
    if (scrollView == self.talentTableView) {
        
        if (self.mainScrollView.contentOffset.y < 175) {
            [self.mainScrollView setContentOffset:scrollView.contentOffset animated:NO];
        }
//        if (self.mainScrollView.contentOffset.y > 175) {
//            //        (self.mainScrollView.contentOffset.y > 175) ? offset.y-- : offset.y++;
//            //        [self.mainScrollView setContentOffset:offset animated:NO];
//            self.talentTableView.scrollEnabled = YES;
//        }
        
//        if (self.talentTableView.contentOffset.y < 0) {
//            CGPoint offset = scrollView.contentOffset;
//            offset.y++;
//        }
        
        CGPoint offset = scrollView.contentOffset;
        CGFloat offsetY = offset.y;
        NSLog(@"tableoffsetY:%f, mainscro:%f", offsetY, self.mainScrollView.contentOffset.y);
    }
    if (self.talentTableView.contentOffset.y < 0 && self.mainScrollView.contentOffset.y >= 175) {
        self.talentTableView.scrollEnabled = NO;
    }
    
    
    
//    if (scrollView == self.mainScrollView) {
//        CGPoint offset = scrollView.contentOffset;
//        
//        (self.mainScrollView.contentOffset.y > 175) ? offset.y-- : offset.y++;
//        [self.mainScrollView setContentOffset:offset animated:NO];
//    }
//    if (scrollView == self.talentTableView) {
//        self.mainScrollView.contentOffset = self.talentTableView.contentOffset;
//        
//    }
}


-(NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    return 50;
}
-(UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"cell"];
    if (!cell) {
        cell = [[UITableViewCell alloc]initWithStyle:UITableViewCellStyleDefault reuseIdentifier:@"cell"];
    }
    cell.textLabel.text = [NSString stringWithFormat:@"%ld", indexPath.row];
    return cell;
}






-(UIScrollView *)mainScrollView {
    if (!_mainScrollView) {
        _mainScrollView = [[UIScrollView alloc]initWithFrame:CGRectMake(0, 0, ScreenWidth, ScreenHeight)];
        _mainScrollView.delegate = self;
        _mainScrollView.backgroundColor = [UIColor greenColor];
        [_mainScrollView setContentSize:CGSizeMake(ScreenWidth, ScreenHeight + 175)];
    }
    return _mainScrollView;
}

-(UIView *)bannerView {
    if (!_bannerView) {
        _bannerView = [[UIView alloc]initWithFrame:CGRectMake(0, 0, ScreenWidth, 175)];
        _bannerView.backgroundColor = [UIColor yellowColor];
    }
    return _bannerView;
}

-(UITableView *)talentTableView {
    if (!_talentTableView) {
        _talentTableView = [[UITableView alloc]initWithFrame:CGRectMake(0, 175, ScreenWidth, ScreenHeight) style:UITableViewStylePlain];
        _talentTableView.delegate = self;
        _talentTableView.dataSource = self;
        [_talentTableView registerClass:[UITableViewCell class] forCellReuseIdentifier:@"cell"];
        _talentTableView.scrollEnabled = NO;
    }
    return _talentTableView;
}

-(UITableView *)friendTableView {
    if (!_friendTableView) {
        _friendTableView = [[UITableView alloc]initWithFrame:CGRectMake(ScreenWidth, 175, ScreenWidth, ScreenHeight - 175) style:UITableViewStylePlain];
        _friendTableView.dataSource = self;
        _friendTableView.delegate = self;
        
    }
    return _friendTableView;
}



@end
